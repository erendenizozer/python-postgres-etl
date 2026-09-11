from pyspark.sql import SparkSession
from pyspark.sql.functions import length, avg


spark = SparkSession.builder \
    .appName("PostsAnalysis") \
    .getOrCreate()


data = [
    (1, "Hello World", "This is a post"),
    (2, "Python", "Learning Python"),
    (3, "Data Engineering", "Learning data engineering"),
    (4, "SQL", "Learning SQL"),
    (5, "Spark", "Learning PySpark")
]

columns = ["id", "title", "body"]

df = spark.createDataFrame(data, columns)

df.show()


df_with_length = df.withColumn(
    "title_length",
    length("title")
)

df_with_length.show()


result = df_with_length.agg(
    avg("title_length").alias("average_title_length")
)

result.show()

spark.stop()