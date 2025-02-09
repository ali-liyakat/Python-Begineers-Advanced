base = 10
height =7
area = (base * height)/2
print(area)
print(type(area))

x = 10
y = 3

print(x + y)
print(x - y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)

print(2 + 4 * 6)  # Associativity and precedence, Use brackets

print(2.3e5)

food = 300.56
rent = 1200.50
bill = 200.80
total = food + rent + bill
print(total)
print(round(total))


# Type Casting

food = '130.40'
rent = '120.30'
total = float(food) + float(rent)   # converts stri gs to float 
print(total)

import math

print(math.sqrt(16))
print(math.floor(10.8))
print(math.ceil(10.4))
print(math.pi)

# Number Representation

print(format(5, 'b'))