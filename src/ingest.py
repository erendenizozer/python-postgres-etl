import argparse
import logging

from .extract import extract_data
from .transform import transform_posts
from .load import create_table, insert_posts, insert_staging_posts, get_max_id

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s"
)

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser()
parser.add_argument("--date", required=True)
args = parser.parse_args()

posts = extract_data()

max_id = get_max_id()

new_posts = []
for post in posts:
    if post["id"] > max_id:
        new_posts.append(posts)

insert_posts(new_posts)

transformed_posts = transform_posts(new_posts)

insert_staging_posts(transformed_posts)

logger.info("ETL completed succesfully!")