import requests

URL = "https://jsonplaceholder.typicode.com/posts"


def extract_data():
    response = requests.get(URL)

    response.raise_for_status()

    return response.json()