import json
import os
import random
import time
import uuid
from datetime import datetime, timezone

from kafka import KafkaProducer

BROKER = os.getenv("KAFKA_BROKER", "redpanda:9092")
TOPIC = os.getenv("TOPIC", "transactions")
EVENTS = int(os.getenv("EVENTS", "2000"))
SLEEP_MS = int(os.getenv("SLEEP_MS", "10"))
DATA_DIR = os.getenv("DATA_DIR", "/app/data")
RAW_FILE = os.path.join(DATA_DIR, "events_snapshot.jsonl")


def make_event() -> dict:
    event_type = random.choices(
        ["view", "add_to_cart", "purchase", "cart_abandon"],
        weights=[55, 25, 15, 5],
        k=1,
    )[0]

    amount = round(random.uniform(10, 1200), 2) if event_type == "purchase" else 0.0

    return {
        "event_id": str(uuid.uuid4()),
        "user_id": random.randint(1, 400),
        "product_id": random.randint(1, 120),
        "event_type": event_type,
        "amount": amount,
        "ts": datetime.now(timezone.utc).isoformat(),
    }


def connect_producer(retries: int = 30, wait: int = 2) -> KafkaProducer:
    for attempt in range(1, retries + 1):
        try:
            return KafkaProducer(
                bootstrap_servers=BROKER,
                value_serializer=lambda v: json.dumps(v).encode("utf-8"),
                key_serializer=lambda v: str(v).encode("utf-8"),
            )
        except Exception as exc:
            print(f"[generator] tentativa {attempt}/{retries} falhou: {exc}")
            time.sleep(wait)
    raise RuntimeError("Não foi possível conectar ao broker")


def main() -> None:
    os.makedirs(DATA_DIR, exist_ok=True)
    producer = connect_producer()

    sent = 0
    with open(RAW_FILE, "a", encoding="utf-8") as f:
        for _ in range(EVENTS):
            event = make_event()
            producer.send(TOPIC, key=event["user_id"], value=event)
            f.write(json.dumps(event, ensure_ascii=False) + "\n")
            sent += 1
            if SLEEP_MS > 0:
                time.sleep(SLEEP_MS / 1000)

    producer.flush()
    producer.close()
    print(f"[generator] {sent} eventos enviados para {TOPIC}")


if __name__ == "__main__":
    main()
