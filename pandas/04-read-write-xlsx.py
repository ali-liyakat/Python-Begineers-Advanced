import pandas as pd

df_movies = pd.read_excel('movies_db.xlsx', 'movies')
print(df_movies.head(4))


df_finance = pd.read_excel('movies_db.xlsx', 'financials')
print(df_movies.head(4))



def standardize_currency(curr):
    if curr =="$$" or curr == "Dollars":
        return "USD"
    return curr
df_finance = pd.read_excel('movies_db.xlsx', 'financials', converters= {
                                                                    'currency': standardize_currency
})
print(df_movies.head(4))


df_merged = pd.merge(df_movies, df_finance, on="movie_id")
print(df_merged.head(4))

# write to an excel file

df_merged.to_excel("movies_merged.xlsx", sheet_name="sheet1", index=False)


df_stock = pd.DataFrame({
    'tickers': ['GOOGLE', 'MICROSOFT', 'AMAZON'],
    'price': [200, 390, 400],
    'eps': [109.90, 230, 120.50],
    'pe': [40, 35, 60]
}
)
print(df_stock)
df_weather = pd.DataFrame({
    'Day': ['01/10/2024', '20/08/2023', '01/10/20'],
    'Temperature': [29, 40, 37],
    'weathr': ['Rainy', 'Sunny', 'Cloud']
})
print(df_weather)

with pd.ExcelWriter("stocks_weather.xlsx") as writer:
    df_stock.to_excel(writer, sheet_name="stocks")
    df_weather.to_excel(writer, sheet_name="weather")
