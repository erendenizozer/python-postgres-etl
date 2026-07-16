from extract import extract_data
from load import create_table, insert_posts

posts = extract_data()

create_table()

insert_posts(posts)

print("ETL completed successfully!")