import json
import os
import time
import uuid

from kafka import KafkaConsumer, TopicPartition

from src.common import get_redis, reset_metrics, process_event, save_rebuild_meta

BROKER = os.getenv("KAFKA_BROKER", "redpanda:9092")
TOPIC = os.getenv("TOPIC", "transactions")


def connect_redis(retries: int = 30, wait: int = 2):
    for attempt in range(1, retries + 1):
        try:
            client = get_redis()
            client.ping()
            return client
        except Exception as exc:
            print(f"[rebuild] redis tentativa {attempt}/{retries} falhou: {exc}")
            time.sleep(wait)
    raise RuntimeError("Não foi possível conectar ao Redis")


def connect_consumer(retries: int = 30, wait: int = 2) -> KafkaConsumer:
    for attempt in range(1, retries + 1):
        try:
            return KafkaConsumer(
                bootstrap_servers=BROKER,
                group_id=f"rebuild-{uuid.uuid4()}",
                enable_auto_commit=False,
                auto_offset_reset="earliest",
                value_deserializer=lambda v: json.loads(v.decode("utf-8")),
                consumer_timeout_ms=2000,
            )
        except Exception as exc:
            print(f"[rebuild] kafka tentativa {attempt}/{retries} falhou: {exc}")
            time.sleep(wait)
    raise RuntimeError("Não foi possível conectar ao broker")


def main() -> None:
    redis_client = connect_redis()
    consumer = connect_consumer()

    partitions = consumer.partitions_for_topic(TOPIC)
    if not partitions:
        print(f"[rebuild] tópico vazio/inexistente: {TOPIC}")
        reset_metrics(redis_client)
        save_rebuild_meta(redis_client, 0, "rebuild executado sem eventos no tópico")
        consumer.close()
        return

    tps = [TopicPartition(TOPIC, p) for p in sorted(partitions)]
    begin_offsets = consumer.beginning_offsets(tps)
    end_offsets = consumer.end_offsets(tps)

    reset_metrics(redis_client)
    consumer.assign(tps)
    for tp in tps:
        consumer.seek_to_beginning(tp)

    target_end = {tp.partition: int(end_offsets.get(tp, 0)) for tp in tps}
    target_count = {
        tp.partition: max(0, int(end_offsets.get(tp, 0)) - int(begin_offsets.get(tp, 0)))
        for tp in tps
    }
    consumed = {tp.partition: 0 for tp in tps}
    total_replayed = 0

    print(f"[rebuild] iniciando replay de {TOPIC} até offsets: {target_end}")

    while True:
        records = consumer.poll(timeout_ms=1000, max_records=500)
        if not records:
            done = all(consumed[p] >= target_count[p] for p in consumed)
            if done:
                break
            continue

        for tp, messages in records.items():
            max_for_partition = target_end.get(tp.partition, 0)
            for msg in messages:
                if msg.offset >= max_for_partition:
                    continue
                process_event(redis_client, msg.value)
                consumed[tp.partition] += 1
                total_replayed += 1

        done = all(consumed[p] >= target_count[p] for p in consumed)
        if done:
            break

    save_rebuild_meta(redis_client, total_replayed, "estado reconstruído via replay do event log")
    consumer.close()

    print(f"[rebuild] concluído: {total_replayed} eventos reprocessados")


if __name__ == "__main__":
    main()
