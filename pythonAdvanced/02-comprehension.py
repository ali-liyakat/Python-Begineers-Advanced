nums = [1,2,3,4,5,6]
sqrs = []
for n in nums:
    sqrs.append(n * n)

print(sqrs)

# List comprehension

sqars = [n * n for n in nums]
print(sqars)

price = [100, 120, 80, 50]
earnings = [0, 15, 40, 2]

pe_ratio = [p/e if e!=0 else -1 for p, e in zip(price,earnings)]
print(pe_ratio)

words = ["banana", "banque", "apple", "orange"]
lengthen =[len(word) for word in words]
print(lengthen)

prices = [200, 190, 50, 40, 79, 300]
dis = [price * 0.9  if price > 100 else price for price in prices]
print(dis)


# dictionary comprehension

names = ["Alice", "Bob", "Mary"]
ages = [28, 30, 42, 50,]

info = {names[i]: ages[i] for i in range(len(names))}
print(info)

# set comprehension

transactions = [
    {"name": "mira", 'amount': 200},
    {"name": "raja", 'amount': 450},
    {"name": "adil", 'amount': 320},
    {"name": "Basit", 'amount': 1400},
    {"name": "mira", 'amount': 700}
]

customers = {trans["name"]for trans in transactions}
print(customers)