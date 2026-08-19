import os
import logging
import psycopg2
from dotenv import load_dotenv
from .transform import transform_posts

load_dotenv()

logger = logging.getLogger(__name__)


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

    try:
        for post in posts:
            cursor.execute(
                """
                INSERT INTO raw_data (id, title, body)
                VALUES (%s, %s, %s)
                ON CONFLICT (id)
                DO UPDATE SET
                title = EXCLUDED.title,
                body = EXCLUDED.body
                """,
                (post["id"], post["title"], post["body"])
            )

        connection.commit()

        logger.info("Loaded %d records into the raw_data", len(posts))
    except Exception as e:
         connection.rollback()
         logger.error("Failed to load %d records into the raw_data: %s", len(posts), e)
         raise
    finally:
        cursor.close()
        connection.close()

def insert_staging_posts(transformed_posts):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            for post in transformed_posts:
                cursor.execute("""INSERT INTO staging_data (id, title,body)
                        VALUES (%s, %s, %s)
                        ON CONFLICT (id)
                        DO UPDATE SET
                        title = EXCLUDED.title,
                        body = EXCLUDED.body""",
                        (post["id"], post["title"], post["body"])
                        )

            connection.commit()

            logger.info("Loaded %d records into the staging_data", len(transformed_posts))

        except Exception as e:
             connection.rollback()
             logger.error("Failed to load %d records into the staging_data: %s", len(transformed_posts), e)
             raise
        finally:
            cursor.close()
            connection.close()
def get_max_id():
     connection = get_connection()
     cursor = connection.cursor()

     cursor.execute(""" SELECT MAX(id) FROM raw_data""")
     result = cursor.fetchone() # Returns (100,) if the max id is 100
     if result is None:
        max_id = 0
     else:
         max_id = result[0] # Now we get the 100
     
     connection.commit()
     connection.close()

     return max_id