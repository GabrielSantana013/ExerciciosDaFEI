import json
import os
import time

from kafka import KafkaConsumer

from src.common import get_redis, init_metrics, process_event

BROKER = os.getenv("KAFKA_BROKER", "redpanda:9092")
TOPIC = os.getenv("TOPIC", "transactions")
GROUP = os.getenv("GROUP", "stream-layer")


def connect_redis(retries: int = 30, wait: int = 2):
    for attempt in range(1, retries + 1):
        try:
            client = get_redis()
            client.ping()
            return client
        except Exception as exc:
            print(f"[processor] redis tentativa {attempt}/{retries} falhou: {exc}")
            time.sleep(wait)
    raise RuntimeError("Não foi possível conectar ao Redis")


def connect_consumer(retries: int = 30, wait: int = 2) -> KafkaConsumer:
    for attempt in range(1, retries + 1):
        try:
            return KafkaConsumer(
                TOPIC,
                bootstrap_servers=BROKER,
                auto_offset_reset="earliest",
                enable_auto_commit=True,
                group_id=GROUP,
                value_deserializer=lambda v: json.loads(v.decode("utf-8")),
            )
        except Exception as exc:
            print(f"[processor] kafka tentativa {attempt}/{retries} falhou: {exc}")
            time.sleep(wait)
    raise RuntimeError("Não foi possível conectar ao broker")


def main() -> None:
    redis_client = connect_redis()
    init_metrics(redis_client)

    consumer = connect_consumer()
    print("[processor] stream processor iniciado")

    for msg in consumer:
        process_event(redis_client, msg.value)


if __name__ == "__main__":
    main()
