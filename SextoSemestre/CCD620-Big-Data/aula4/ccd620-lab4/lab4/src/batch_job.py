import os

import duckdb

DATA_DIR = os.getenv("DATA_DIR", "/app/data")
RAW_FILE = os.path.join(DATA_DIR, "events.jsonl")
DB_FILE = os.path.join(DATA_DIR, "lambda.duckdb")


def main() -> None:
    if not os.path.exists(RAW_FILE):
        print(f"[batch] arquivo não encontrado: {RAW_FILE}")
        return

    con = duckdb.connect(DB_FILE)

    con.execute(
        """
        CREATE OR REPLACE TABLE batch_metrics AS
        SELECT
            COUNT(*) AS events_total,
            SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) AS purchases_total,
            ROUND(SUM(CASE WHEN event_type = 'purchase' THEN amount ELSE 0 END), 2) AS purchase_amount_total,
            SUM(CASE WHEN event_type = 'cart_abandon' THEN 1 ELSE 0 END) AS cart_abandon_total,
            MAX(ts) AS last_event_ts
        FROM read_json_auto(?);
        """,
        [RAW_FILE],
    )

    con.close()
    print(f"[batch] métricas recalculadas em {DB_FILE}")


if __name__ == "__main__":
    main()
