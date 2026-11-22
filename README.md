# pyspark-movie-reviews
# PySpark Movie Reviews

This is a small project I made for my Data course homework. It uses PySpark to go through the IMDB dataset of 50,000 movie reviews and pull out a few basic insights.

## What the code does

- Loads the reviews from the CSV file into a Spark DataFrame
- Prints the schema and the total number of reviews
- Counts how many reviews are positive and how many are negative
- Calculates the average review length for each sentiment
- Finds the 10 most common words (ignoring very short ones)

## What I found

- The dataset has 50,000 reviews, split evenly into 25,000 positive and 25,000 negative.
- Positive reviews are slightly longer on average (about 1325 characters) than negative ones (about 1294).
- The top words are mostly common ones like "this", "that" and "with", and "movie" and "film" show up a lot too, which makes sense for movie reviews.

## How to run it

1. Download the dataset from Kaggle: IMDB Dataset of 50K Movie Reviews
2. Put `IMDB Dataset.csv` in the same folder as `movie_reviews.py`
3. Install PySpark with `pip install pyspark` (you also need Java 17 or 21)
4. Run `python movie_reviews.py`

## Note

The dataset file is not included in this repo because of its size, so it has to be downloaded separately.
