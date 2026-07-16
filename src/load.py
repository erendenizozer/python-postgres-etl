import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )


def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS raw_data (
            id SERIAL PRIMARY KEY,
            title TEXT,
            body TEXT
        );
    """)

    connection.commit()

    cursor.close()
    connection.close()


def insert_posts(posts):
    connection = get_connection()
    cursor = connection.cursor()

    for post in posts:
        cursor.execute(
            """
            INSERT INTO raw_data (title, body)
            VALUES (%s, %s)
            """,
            (post["title"], post["body"])
        )

    connection.commit()

    cursor.close()
    connection.close()