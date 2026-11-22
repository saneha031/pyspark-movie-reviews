from pyspark.sql import SparkSession
from pyspark.sql.functions import col, length, lower, explode, split

spark = SparkSession.builder.appName("MovieReviews").getOrCreate()

df = spark.read.csv("IMDB Dataset.csv", header=True, inferSchema=True, multiLine=True, escape='"')

df.printSchema()
print("Total reviews:", df.count())

df.groupBy("sentiment").count().show()

df = df.withColumn("review_length", length(col("review")))
df.groupBy("sentiment").avg("review_length").show()

words = df.select(explode(split(lower(col("review")), "\\W+")).alias("word"))
words.filter(length(col("word")) > 3).groupBy("word").count().orderBy(col("count").desc()).show(10)

spark.stop()