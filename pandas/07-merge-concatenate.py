import pandas as pd

india_weather = pd.DataFrame({
    'city': ['Mumbai', 'Bangalore', 'Delhi'],
    'temperature': [38, 27, 42],
    'humidity': [90, 75, 80]
})
print(india_weather)
print("\n================")

us_weather = pd.DataFrame({
    'city': ['New york', 'Chicago', 'orolando'],
    'temperature': [40, 36, 40],
    'humidity': [460, 50, 76]
})
print(us_weather)
print("\n================================")


# Concat function
new_df = pd.concat([india_weather, us_weather])
print(new_df)
print("\n================================")



new_df = pd.concat([india_weather, us_weather], ignore_index=True)
print(new_df)
print("\n================================")


new_df = pd.concat([india_weather, us_weather],  keys=["India", "USA"],)
print(new_df)
print("================================")

print(new_df.loc["USA"])


temp_df = pd.DataFrame({
    'city': ['Mumbai', 'Bangalore', 'Delhi'],
    'temperature': [38, 27, 42]
}, index=[0,1,2])
print(temp_df)

wind_df = pd.DataFrame({
    'city': ['Delhi', 'Mumbai'],
    'windspeed': [9, 12]
}, index=[2,0])
print(wind_df)
print("\n================================================")

print(pd.concat([temp_df,wind_df], axis=1))





# merge function

df1 = pd.DataFrame({
    'city': ['new york', 'chicago', 'orlando'],
    'temperature': [21, 15, 34]
})
print(df1)
print("\n================================================")

df2 = pd.DataFrame({
    'city': ['new york', 'chicago', 'orlando'],
    'humidity': [29, 23, 45]
})
print(df2)
print("\n================================================")

merged_df = pd.merge(df1, df2, on="city")
print(merged_df)


df11 = pd.DataFrame({
    'city': ['new york', 'chicago', 'orlando','baltimore'],
    'temperature': [21, 15, 34, 28]
})

df22 = pd.DataFrame({
    'city': ['new york', 'chicago', 'san diego'],
    'humidity': [70, 55, 80]
})

print(pd.merge(df11, df22, on="city", how="inner"))
print("\n================================")

print(pd.merge(df11, df22, on="city", how="left"))
print("\n==================================")


print(pd.merge(df11, df22, on="city", how="right"))
print("\n============================================")


print(pd.merge(df11, df22, on="city", how="outer"))
print("\n============================================")
