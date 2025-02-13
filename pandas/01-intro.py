import csv


# Data Analysis in Python
def calculate_rating(data, industry = None):
    ratings = []
    for row in data:
        if row[3]!= 'NULL' and (not industry or row[1]== industry):
            ratings.append(float(row[3]))
    
    max_ratings = max(ratings)
    min_ratings = min(ratings)
    avg_ratings = sum(ratings)/len(ratings)
    return max_ratings, min_ratings, avg_ratings



with open('movies.csv') as f:
    data = list(csv.reader(f))
    header = data[0]
    data = data[1:]
    

    max_ratings, min_ratings, avg_ratings = calculate_rating(data)
    print(f" All records: Min rating= {min_ratings}, Max rating= {max_ratings}, Average rating= {avg_ratings}.")

    max_ratings, min_ratings, avg_ratings = calculate_rating(data, industry='Bollywood')
    print(f" Bollywood rating: Min rating= {min_ratings}, Max rating = {max_ratings}, Average rating: {avg_ratings}")

    max_ratings, min_ratings, avg_ratings = calculate_rating(data, industry='Hollywood')
    print(f" Hollywood rating: Min rating= {min_ratings}, Max rating = {max_ratings}, Average rating= {avg_ratings}")



# Data Analysis using Pandas
import pandas as pd

df = pd.read_csv("movies.csv")
# print(df)

# prints first 5 values
print(df.head())


# prints last 5 values
print(df.tail())

# print any random values
print(df.sample(3))

# slicing
print(df[3:6])

print(df.shape)

print(df.imdb_rating)
print(df["imdb_rating"])

print(df.imdb_rating.min(), df.imdb_rating.max(), df.imdb_rating.mean())

bollywood = df[df.industry == 'Bollywood']
print(bollywood)

print(bollywood.imdb_rating.min(), bollywood.imdb_rating.max(), bollywood.imdb_rating.mean())


hollywood = df[df.industry == 'Hollywood']
print(hollywood)

print(hollywood.imdb_rating.min(), hollywood.imdb_rating.max(), hollywood.imdb_rating.mean())

