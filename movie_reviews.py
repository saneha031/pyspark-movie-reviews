from pyspark.sql import SparkSession
from pyspark.sql.functions import col, length, trim

spark = SparkSession.builder.appName("MovieReviews").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

# 1. Load the dataset
df = spark.read.csv("IMDB Dataset.csv", header=True, inferSchema=True,
                    multiLine=True, escape='"')

# 2. Explore the data
print("Schema:")
df.printSchema()
print("First 5 rows:")
df.show(5, truncate=80)

# 3. Clean the data: remove rows with null or empty reviews
rows_before = df.count()
df_clean = df.dropna(subset=["review"]).filter(trim(col("review")) != "")
rows_after = df_clean.count()
print("Rows before cleaning:", rows_before)
print("Rows after cleaning:", rows_after)

# 4. Analyze the data
print("Total number of reviews:", df_clean.count())
print("Positive and negative reviews:")
df_clean.groupBy("sentiment").count().show()

# 5. Transform the data
df_transformed = df_clean.withColumn("review_length", length(col("review")))
print("Reviews longer than 500 characters:")
long_reviews = df_transformed.filter(col("review_length") > 500)
long_reviews.select("review_length", "sentiment", "review").show(10, truncate=60)
print("Count of reviews longer than 500 characters:", long_reviews.count())

# 6. Save the cleaned and transformed DataFrame as a new CSV
try:
    df_transformed.coalesce(1).write.mode("overwrite") \
        .option("header", True).csv("cleaned_reviews_output")
    print("Saved with Spark to the folder: cleaned_reviews_output")
except Exception:
    df_transformed.toPandas().to_csv("cleaned_reviews.csv", index=False)
    print("Saved with pandas to: cleaned_reviews.csv")

spark.stop()