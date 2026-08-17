import requests
import logging

logger = logging.getLogger(__name__)

URL = "https://jsonplaceholder.typicode.com/posts"


def extract_data():
    response = requests.get(URL)

    response.raise_for_status()

    posts = response.json()

    logger.info("Extracted %d posts", len(posts))

    return posts



