import pandas as pd

df = pd.read_csv("weather_by_cities.csv")
print(df)

print(df[df.city=="new york"].temperature.max())

g = df.groupby("city")
for city, data in g:
    print("city: " ,city)
    print("max temp: " ,data.temperature.max())
    print("\n=====")


print(g.get_group("mumbai"))

print(g.max())

print(g.min())

print(g.describe())

print(g.size())



def grouper(df, idx, col):
    if 80 <= df[col].loc[idx] <= 90:
        return "80-90"
    elif 50 <= df[col].loc[idx] <= 60:
        return "50-60"
    else:
        return 'Others'

gr = df.groupby(lambda idx: grouper(df, idx, 'temperature'))
for key, data in gr:
    print("key", key)
    print("data", data)
    print("\n====")