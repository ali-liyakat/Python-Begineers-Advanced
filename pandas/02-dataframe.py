import pandas as pd

df = pd. read_csv("movies.csv")
print(df.head())

# shape 
print(df.shape)

# columns
print(df.columns)

print(df.industry.unique())

print(df.language.unique())

print(df.industry.value_counts())

print(df.language.value_counts())

# subset of dataframe
# column filtering
print(df[["title", "imdb_rating", "industry"]])

# row filtering
print(df[df.release_year > 2005])


print(df[(df.release_year > 2005) & (df.release_year < 2020)])

print(df[df.studio == "Marvel Studios"])

print(df.describe())

print(df.info())

print(df[(df.imdb_rating == df.imdb_rating.max()) | (df.imdb_rating == df.imdb_rating.min())])


# Generate new column names

df["age"] = df['release_year']. apply(lambda x: 2024 - x)
print(df.head(3))

df['profit'] = df.apply(lambda x: x['revenue'] - x['budget'], axis=1)
print(df.head(3))



# index
print(df.index)

df.set_index('title', inplace=True)
print(df.head(3))

print(df.index)

print(df.loc["Pather Panchali"])

print(df.loc[["Pather Panchali", "Doctor Strange in the Multiverse of Madness"]])


# integer index

print(df.iloc[0])

print(df.iloc[2:6])

df.reset_index(inplace= True)
print(df.head(3))