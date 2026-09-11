import logging
import time

from src.extract import extract_data
from src.load import insert_posts, insert_staging_posts
from src.transform import transform_posts
from src.quality import run_quality_checks


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s"
)

logger = logging.getLogger(__name__)


def run_with_retry(task, task_name, retries=3):
    for attempt in range(1, retries + 1):
        try:
            logger.info(
                "Starting task: %s (attempt %d/%d)",
                task_name,
                attempt,
                retries
            )

            result = task()

            logger.info("Task completed: %s", task_name)

            return result

        except Exception as e:
            logger.error(
                "Task failed: %s - %s",
                task_name,
                e
            )

            if attempt == retries:
                logger.error(
                    "Task failed permanently: %s",
                    task_name
                )
                raise

            logger.info(
                "Retrying %s in 2 seconds...",
                task_name
            )

            time.sleep(2)


def extract_task():
    return extract_data()


def load_task(posts):
    insert_posts(posts)


def transform_task(posts):
    transformed_posts = transform_posts(posts)
    insert_staging_posts(transformed_posts)


def quality_task():
    run_quality_checks()


def run_pipeline():
    logger.info("========== PIPELINE START ==========")

    # 1. EXTRACT
    posts = run_with_retry(
        extract_task,
        "extract",
        retries=3
    )

    # 2. LOAD
    run_with_retry(
        lambda: load_task(posts),
        "load",
        retries=3
    )

    # 3. TRANSFORM
    run_with_retry(
        lambda: transform_task(posts),
        "transform",
        retries=3
    )

    # 4. DATA QUALITY
    run_with_retry(
        quality_task,
        "quality_checks",
        retries=3
    )

    logger.info("========== PIPELINE COMPLETED ==========")


if __name__ == "__main__":
    run_pipeline()