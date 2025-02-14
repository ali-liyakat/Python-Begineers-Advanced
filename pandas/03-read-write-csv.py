import pandas as pd

df = pd.read_csv("stock_data.csv")
print(df.head())

df = pd.read_csv("stock_data.csv", skiprows=1)
print(df.head())

df = pd.read_csv("stock_data.csv", header=1)
print(df.head())

# custom column names
df = pd.read_csv("stock_data.csv", header=1, names=['company', 'eps', 'revenue', 'price', 'people'])
print(df.head())


# Read specific number of rows
df = pd.read_csv("stock_data.csv", header=1, nrows=2)
print(df)


# conver to NaN
df = pd.read_csv("stock_data.csv", header=1, na_values= {
                                                'eps': ['not available'], 
                                                'revenue':[-1], 
                                                'price':['n.a.','not available'],
                                                'people':['n.a.','not available']})
print(df)


#for All at a time
df = pd.read_csv("stock_data.csv", header=1, na_values=['n.a.','not available', -1])
print(df)


df['pe'] = df['price']/df['eps']
print(df)


# write to a CSV file
df.to_csv('pe.csv')

# remove index and header fields
df.to_csv('pe1.csv', index=False, header=False)


