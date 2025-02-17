# ITERATORS

prices = []

with open("pricing.txt","r") as f:
    for line in f:
        ticker, country, price, date = line.split("|")
        prices.append({
            'ticker': ticker,
            'country': country,
            'price': float(price),
            'date': date.strip()
        })

print(prices[:2])

f = open("pricing.txt", "r")
iterator = iter(f)
print(iterator)

print(next(iterator))
print(next(iterator))


class RemoteControl:
    def __init__(self):
        self.channels = ["NDTV", "CNN", "HBO"]
        self.index = -1

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]
    
    def __iter__(self):
        return self
    
rc = RemoteControl()
for channel in rc:
    print(channel)
print("\n================================")
rc1 = RemoteControl()
print(next(rc1))
print(next(rc1))


# GENERATORS

def remote_control():
    yield "CNN"
    yield "NDTV"
    yield "HBO"

rm = remote_control()
print(type(rm))

for channel in rm:
    print(channel)


print("\n================================")
r = remote_control()
print(next(r))
print(next(r))



def get_company_data():
    data = []
    for i in range(3):
        with open(f"stock_{i+1}.txt","r") as f:
            content = f.read()
            data.append(content)
    return data 

print(get_company_data())
print("\n================================================")

def get_company_data():
    data = []
    for i in range(3):
        with open(f"stock_{i+1}.txt","r") as f:
            content = f.read()
            yield content

for comp_data in get_company_data():
    print(comp_data)


# Fibonacci series

def fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

fib_gen = fibo()
for nums in range(10):
    print(next(fib_gen))