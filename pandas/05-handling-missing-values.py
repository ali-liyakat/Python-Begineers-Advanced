import pandas as pd
import numpy as np

df = pd.read_csv("weather_data.csv", parse_dates=['day'])
print(df)

df.set_index('day', inplace=True)
print(df)


# fill NaN values

df.fillna(0)    #inplace=True
print(df)


df.fillna({
    'temperature': df.temperature.mean(),
    'windspeed': df.windspeed.mean(),
    'event': 'No Event'
})      # inplace=True
print(df)


df.fillna(method='ffill') # inplace=True
print(df)

df.fillna(method='bfill') # inplace
print(df)

df.fillna(method='ffill', limit=1) # inplace=True
print(df)

df.interpolate() # inplace=True
print(df)


# Drop NAN values

df.dropna() # inplace=True
print(df)

df.dropna(how='all') # inplace=True
print(df)


df.dropna(thresh=2) # inplace=True
print(df)
print('\n================================')
print('\n================================')
print('\n================================')
print('\n================================')


# handling Missing values

df = pd.read_csv("weather2_data.csv")
print(df)

df.set_index('day', inplace=True)
print(df)

df.replace(-99999, 0)   # inplace=True
print(df)

df.replace(to_replace=[-99999, -88888], value=np.nan)   # inplace=True
print(df)

df.replace({
    'temperature': -99999,
    'windspeed': [-99999, -88888],
    'event': 'no event'
}, np.nan) # inplace=True
print(df)


df.replace({
    -99999: np.nan,
    -88888: np.nan,
    'no event': 'Sunny'
}, inplace=True)
print(df)