import os
from datetime import datetime, timezone

import redis

METRICS_KEY = "metrics:realtime"
REBUILD_META_KEY = "kappa:rebuild_meta"


def default_metrics() -> dict:
    return {
        "events_total": 0,
        "purchases_total": 0,
        "purchase_amount_total": 0.0,
        "cart_abandon_total": 0,
    }


def get_redis() -> redis.Redis:
    host = os.getenv("REDIS_HOST", "redis")
    port = int(os.getenv("REDIS_PORT", "6379"))
    return redis.Redis(host=host, port=port, decode_responses=True)


def init_metrics(r: redis.Redis) -> None:
    if not r.exists(METRICS_KEY):
        r.hset(METRICS_KEY, mapping=default_metrics())


def reset_metrics(r: redis.Redis) -> None:
    r.delete(METRICS_KEY)
    init_metrics(r)


def process_event(r: redis.Redis, event: dict) -> None:
    pipe = r.pipeline()
    pipe.hincrby(METRICS_KEY, "events_total", 1)

    if event.get("event_type") == "purchase":
        pipe.hincrby(METRICS_KEY, "purchases_total", 1)
        pipe.hincrbyfloat(METRICS_KEY, "purchase_amount_total", float(event.get("amount", 0.0)))

    if event.get("event_type") == "cart_abandon":
        pipe.hincrby(METRICS_KEY, "cart_abandon_total", 1)

    pipe.execute()


def save_rebuild_meta(r: redis.Redis, events_replayed: int, note: str) -> None:
    r.hset(
        REBUILD_META_KEY,
        mapping={
            "events_replayed": events_replayed,
            "last_rebuild_ts": datetime.now(timezone.utc).isoformat(),
            "note": note,
        },
    )
