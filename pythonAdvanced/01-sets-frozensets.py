# sets:- ordered list of unique elements

myset = set([1,2,3,5,3,4,6,7,4,2])
print(myset)

print(list(myset))

# print(myset[0]) # Not allowed

menu = set(["idli", "biryani", "dosa"])
menu.add("pizza")
print(menu)

print("dosa" in menu)

menu.remove("dosa")
print(menu)


# frozenset

menu = frozenset(["idli", "biryani", "dosa"])
# menu.add("pizza")  Not allowed
print("burger" in menu)
print(menu)

transactions = [
    {"name": "mira", 'amount': 200},
    {"name": "raja", 'amount': 450},
    {"name": "adil", 'amount': 320},
    {"name": "Basit", 'amount': 1400},
    {"name": "mira", 'amount': 700}
]
customers =set()
for trans in transactions:
    customers.add(trans["name"])

print(customers)

print(list(customers))

a = {"mira", "basit", "raja", "hani", "arun"}
b = {"anuj", "mira", "bhat", "ali", "hani"}

print(a & b)    # intersection
print(a.intersection(b)) # intersection


print(a|b)  # union
print(a.union(b))

print(a - b) # difference