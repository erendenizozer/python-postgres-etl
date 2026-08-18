import requests
import logging

logger = logging.getLogger(__name__)

URL = "https://jsonplaceholder.typicode.com/posts"


def extract_data():
    try:
        response = requests.get(URL)
        response.raise_for_status()
    except Exception as e:
        logger.error("Failed to extract data: %s", e)
        raise

    posts = response.json()

    logger.info("Extracted %d posts", len(posts))

    return posts



