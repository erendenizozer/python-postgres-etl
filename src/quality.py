import logging

from src.load import get_connection

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s"
)

logger = logging.getLogger(__name__)


def check_row_count():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM staging_data;")
    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    if count == 0:
        raise ValueError("Data quality failed: staging_data is empty.")

    logger.info(f"Row count check passed: {count} rows")
    return count


def check_duplicate_ids():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, COUNT(*)
        FROM staging_data
        GROUP BY id
        HAVING COUNT(*) > 1;
    """)

    duplicates = cursor.fetchall()

    cursor.close()
    conn.close()

    if duplicates:
        raise ValueError(
            f"Data quality failed: duplicate IDs found: {duplicates}"
        )

    logger.info("Duplicate ID check passed.")
    return True


def check_nulls():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            COUNT(*) AS total_rows,
            COUNT(id) AS id_count,
            COUNT(title) AS title_count,
            COUNT(body) AS body_count
        FROM staging_data;
    """)

    total, ids, titles, bodies = cursor.fetchone()

    cursor.close()
    conn.close()

    if total == 0:
        raise ValueError("Data quality failed: table is empty.")

    null_id_ratio = (total - ids) / total
    null_title_ratio = (total - titles) / total
    null_body_ratio = (total - bodies) / total

    logger.info(f"id NULL ratio: {null_id_ratio:.2%}")
    logger.info(f"title NULL ratio: {null_title_ratio:.2%}")
    logger.info(f"body NULL ratio: {null_body_ratio:.2%}")

    if null_id_ratio > 0:
        raise ValueError("Data quality failed: id contains NULL values.")

    if null_title_ratio > 0:
        raise ValueError("Data quality failed: title contains NULL values.")

    if null_body_ratio > 0:
        raise ValueError("Data quality failed: body contains NULL values.")

    logger.info("NULL check passed.")
    return True


def run_quality_checks():
    logger.info("Starting data quality checks...")

    check_row_count()
    check_duplicate_ids()
    check_nulls()

    logger.info("All data quality checks passed.")


if __name__ == "__main__":
    run_quality_checks()