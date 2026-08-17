from extract import extract_data
from transform import transform_posts
from load import create_table, insert_posts, insert_staging_posts

posts = extract_data()

insert_posts(posts)

transformed_posts = transform_posts(posts)

insert_staging_posts(transformed_posts)

print("ETL completed successfully!")