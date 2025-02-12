# Exception Handling

x = input("enter number 1: ")
y = input("enter number 2: ")

d = 0
try:
    d = int(x) / int(y)
    a ='baby' + 25
except ZeroDivisionError as ze:
    print("Error: ", ze)
    d = -1

except TypeError as te:
    print("Error: ", te)
    d = -1

except Exception as e:
    print("Error: ", e)
    d = -1

print("Division is: ", d)

file = None
try:
    file = open("file.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found")
finally:
    if file:
        file.close()
    print("File closed")




# Custom Exceptions
class insufficientBalance(Exception):
    pass


balance = 0
def deposit(amount):
    global balance
    if amount < 0:
        raise ValueError("Amount should be positive")
    balance += amount


def withdraw(amount):
    global balance
    if amount > balance:
        raise insufficientBalance("Insufficient balance")
    balance -= amount

deposit(100)
deposit(10)
withdraw(200)
# withdraw(100)
print("Balance: ", balance)