import json
import os
from collections import deque

from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from kafka import KafkaConsumer, TopicPartition

from src.common import METRICS_KEY, REBUILD_META_KEY, get_redis

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "redpanda:9092")
TOPIC = os.getenv("TOPIC", "transactions")
STREAM_GROUP = os.getenv("GROUP", "stream-layer")
DATA_DIR = os.getenv("DATA_DIR", "/app/data")
SNAPSHOT_FILE = os.path.join(DATA_DIR, "events_snapshot.jsonl")

app = FastAPI(title="Kappa Lab API", version="1.0.0")


def _safe_snapshot(fn, **kwargs):
    try:
        return fn(**kwargs)
    except Exception as exc:
        return {"error": str(exc)}


def get_kafka_consumer(group_id: str | None = None) -> KafkaConsumer:
    return KafkaConsumer(
        bootstrap_servers=KAFKA_BROKER,
        group_id=group_id,
        enable_auto_commit=False,
        api_version_auto_timeout_ms=5000,
        request_timeout_ms=15000,
    )


def read_last_events(limit: int) -> list[dict]:
    if not os.path.exists(SNAPSHOT_FILE):
        return []

    rows = deque(maxlen=max(1, limit))
    with open(SNAPSHOT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue

    return list(rows)


def file_line_count(path: str) -> int:
    if not os.path.exists(path):
        return 0
    with open(path, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)


@app.get("/", response_class=HTMLResponse)
def root_dashboard(refresh: int = Query(default=5, ge=0, le=300)):
    kappa = _safe_snapshot(kappa_view)
    topic = _safe_snapshot(kafka_topic_info)
    group = _safe_snapshot(kafka_group_info)

    endpoints = [
        ("/health", "Status básico da API"),
        ("/realtime", "Read model em Redis atualizado pelo stream processor"),
        ("/kappa-view", "Visão Kappa (estado atual + metadados de replay)"),
        ("/stored/raw?limit=20", "Amostra local dos eventos gerados (debug didático)"),
        ("/kafka/topic", "Partições e offsets do tópico"),
        ("/kafka/group", "Offset commitado e lag estimado do consumer group"),
    ]

    links_html = "".join(
        f'<li><a href="{path}">{path}</a> — {desc}</li>' for path, desc in endpoints
    )

    refresh_meta = f'<meta http-equiv="refresh" content="{refresh}" />' if refresh > 0 else ""
    refresh_label = (
        f"a cada {refresh} segundos" if refresh > 0 else "desativada (use ?refresh=5, por exemplo)"
    )

    page = f"""
    <html lang="pt-br">
      <head>
        <meta charset="utf-8" />
        {refresh_meta}
        <title>Kappa Lab API</title>
        <style>
          body {{ font-family: Arial, sans-serif; margin: 24px; line-height: 1.4; }}
          h1, h2 {{ margin-bottom: 8px; }}
          pre {{ background: #f5f5f5; padding: 12px; border-radius: 8px; overflow-x: auto; }}
          .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap: 12px; }}
          .card {{ border: 1px solid #ddd; border-radius: 8px; padding: 12px; }}
        </style>
      </head>
      <body>
        <h1>Laboratório Kappa — Dashboard</h1>
        <p><strong>Atualização automática:</strong> {refresh_label} (pode ser alterado com <code>/?refresh=2</code>).</p>

        <h2>Endpoints disponíveis</h2>
        <ul>{links_html}</ul>

        <h2>Resumo atual</h2>
        <div class="grid">
          <div class="card">
            <h3>/kappa-view</h3>
            <pre>{json.dumps(kappa, ensure_ascii=False, indent=2)}</pre>
          </div>
          <div class="card">
            <h3>/kafka/topic</h3>
            <pre>{json.dumps(topic, ensure_ascii=False, indent=2)}</pre>
          </div>
          <div class="card">
            <h3>/kafka/group</h3>
            <pre>{json.dumps(group, ensure_ascii=False, indent=2)}</pre>
          </div>
        </div>
      </body>
    </html>
    """

    return page


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/realtime")
def realtime():
    r = get_redis()
    data = r.hgetall(METRICS_KEY) or {}
    return {
        "events_total": int(float(data.get("events_total", 0))),
        "purchases_total": int(float(data.get("purchases_total", 0))),
        "purchase_amount_total": float(data.get("purchase_amount_total", 0.0)),
        "cart_abandon_total": int(float(data.get("cart_abandon_total", 0))),
    }


@app.get("/stored/raw")
def stored_raw(limit: int = 20):
    safe_limit = min(max(limit, 1), 200)
    events = read_last_events(safe_limit)
    return {
        "raw_file": SNAPSHOT_FILE,
        "events_in_file": file_line_count(SNAPSHOT_FILE),
        "returned": len(events),
        "events": events,
    }


@app.get("/kafka/topic")
def kafka_topic_info():
    consumer = get_kafka_consumer()
    try:
        partitions = consumer.partitions_for_topic(TOPIC)
        if not partitions:
            return {
                "topic": TOPIC,
                "broker": KAFKA_BROKER,
                "exists": False,
                "partitions": [],
                "messages_total_estimate": 0,
            }

        tps = [TopicPartition(TOPIC, p) for p in sorted(partitions)]
        begins = consumer.beginning_offsets(tps)
        ends = consumer.end_offsets(tps)

        parts = []
        total = 0
        for tp in tps:
            begin = int(begins.get(tp, 0))
            end = int(ends.get(tp, 0))
            qty = max(0, end - begin)
            total += qty
            parts.append(
                {
                    "partition": tp.partition,
                    "begin_offset": begin,
                    "end_offset": end,
                    "messages_estimate": qty,
                }
            )

        return {
            "topic": TOPIC,
            "broker": KAFKA_BROKER,
            "exists": True,
            "partition_count": len(parts),
            "messages_total_estimate": total,
            "partitions": parts,
        }
    finally:
        consumer.close()


@app.get("/kafka/group")
def kafka_group_info(group_id: str = STREAM_GROUP):
    consumer = get_kafka_consumer(group_id=group_id)
    try:
        partitions = consumer.partitions_for_topic(TOPIC)
        if not partitions:
            return {
                "group_id": group_id,
                "topic": TOPIC,
                "exists": False,
                "total_lag_estimate": 0,
                "partitions": [],
            }

        tps = [TopicPartition(TOPIC, p) for p in sorted(partitions)]
        consumer.assign(tps)
        ends = consumer.end_offsets(tps)

        parts = []
        total_lag = 0
        for tp in tps:
            committed = consumer.committed(tp)
            committed = int(committed) if committed is not None else 0
            end = int(ends.get(tp, 0))
            lag = max(0, end - committed)
            total_lag += lag
            parts.append(
                {
                    "partition": tp.partition,
                    "committed_offset": committed,
                    "end_offset": end,
                    "lag_estimate": lag,
                }
            )

        return {
            "group_id": group_id,
            "topic": TOPIC,
            "exists": True,
            "total_lag_estimate": total_lag,
            "partitions": parts,
        }
    finally:
        consumer.close()


@app.get("/kappa-view")
def kappa_view():
    r = get_redis()
    meta = r.hgetall(REBUILD_META_KEY) or {}

    return {
        "realtime": realtime(),
        "rebuild_meta": {
            "events_replayed": int(float(meta.get("events_replayed", 0))) if meta else 0,
            "last_rebuild_ts": meta.get("last_rebuild_ts"),
            "note": meta.get("note"),
        },
        "note": "Visão Kappa com pipeline único em streaming e replay do event log",
    }
