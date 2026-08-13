from extract import extract_data
from transform import transform_posts
from load import create_table, insert_posts

posts = extract_data()

transformed_posts = transform_posts(posts)

create_table()

insert_posts(transformed_posts)

print("ETL completed successfully!")