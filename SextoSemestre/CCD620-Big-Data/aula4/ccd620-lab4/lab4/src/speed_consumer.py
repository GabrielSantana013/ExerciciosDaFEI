import json
import os
import time

import redis
from kafka import KafkaConsumer

BROKER = os.getenv("KAFKA_BROKER", "redpanda:9092")
TOPIC = os.getenv("TOPIC", "transactions")
GROUP = os.getenv("GROUP", "speed-layer")
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))


METRICS_KEY = "metrics:realtime"


def connect_redis(retries: int = 30, wait: int = 2) -> redis.Redis:
    for attempt in range(1, retries + 1):
        try:
            client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
            client.ping()
            return client
        except Exception as exc:
            print(f"[speed] redis tentativa {attempt}/{retries} falhou: {exc}")
            time.sleep(wait)
    raise RuntimeError("Não foi possível conectar ao Redis")


def connect_consumer(retries: int = 30, wait: int = 2) -> KafkaConsumer:
    for attempt in range(1, retries + 1):
        try:
            consumer = KafkaConsumer(
                TOPIC,
                bootstrap_servers=BROKER,
                auto_offset_reset="earliest",
                enable_auto_commit=True,
                group_id=GROUP,
                value_deserializer=lambda v: json.loads(v.decode("utf-8")),
            )
            return consumer
        except Exception as exc:
            print(f"[speed] kafka tentativa {attempt}/{retries} falhou: {exc}")
            time.sleep(wait)
    raise RuntimeError("Não foi possível conectar ao broker")


def init_metrics(r: redis.Redis) -> None:
    defaults = {
        "events_total": 0,
        "purchases_total": 0,
        "purchase_amount_total": 0.0,
        "cart_abandon_total": 0,
    }
    if not r.exists(METRICS_KEY):
        r.hset(METRICS_KEY, mapping=defaults)


def process_event(r: redis.Redis, event: dict) -> None:
    pipe = r.pipeline()
    pipe.hincrby(METRICS_KEY, "events_total", 1)

    if event.get("event_type") == "purchase":
        pipe.hincrby(METRICS_KEY, "purchases_total", 1)
        pipe.hincrbyfloat(METRICS_KEY, "purchase_amount_total", float(event.get("amount", 0.0)))

    if event.get("event_type") == "cart_abandon":
        pipe.hincrby(METRICS_KEY, "cart_abandon_total", 1)

    pipe.execute()


def main() -> None:
    r = connect_redis()
    init_metrics(r)
    consumer = connect_consumer()

    print("[speed] consumidor iniciado")
    for msg in consumer:
        process_event(r, msg.value)


if __name__ == "__main__":
    main()
