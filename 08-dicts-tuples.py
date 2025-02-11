# Tuples
# Tuples are similar to lists, but they are immutable, meaning that the values in a tuple cannot be changed.
my_tup = (1, 2,)
print(my_tup)
print(my_tup[0])

# function returning a tuple
def pe_pd_ratio(price, eps, book_value):
    pe = price / eps
    pb = price / book_value
    return pe, pb

pe, pb = pe_pd_ratio(100, 10, 50)
print(pe, pb)


# Dictionary
# A dictionary is an unordered collection of items. Each item in a dictionary is a key-value pair.

stock_prices = {'AAPL': 200, 'GOOGL': 1000, 'MSFT': 150, 'AMZN': 1800}
print(stock_prices)
print(stock_prices['AAPL'])

print(stock_prices.get('GOOGL'))
print(stock_prices.get('ABBL'))

# add a new key-value pair
stock_prices['ABBL'] = 100
print(stock_prices)

# remove a key-value pair
stock_prices.pop('AAPL')
print(stock_prices)

# delete a key
del stock_prices['GOOGL']
print(stock_prices)

# check if a key exists
print('AAPL' in stock_prices)

# get all keys
print(stock_prices.keys())

# get all values
print(stock_prices.values())

# get all key-value pairs
print(stock_prices.items())

# loop through a dictionary
for key, value in stock_prices.items():
    print(key, value)


# Nested dictionary
# A dictionary can contain dictionaries as values.
apple_revenue = {'USA':{'mac':100, 'iphone':200, 'ipad':300},
                 'China':{'mac':50, 'iphone':100, 'ipad':150},
                 'India':{'mac':10, 'iphone':20, 'ipad':30}}

for country, country_revenue in apple_revenue.items():
    for product, revenue in country_revenue.items():
        print(country, product, revenue)
