# check odd even number


# if else condition:
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")



# nested if else condition:
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number")
    if num % 4 == 0:
        print(f"{num} is a multiple of 4")
    else:
        print(f"{num} is not a multiple of 4")
else:
    print(f"{num} is an odd number")



# elif condition:
num = int(input("Enter a number: "))
if num % 4 == 0:
    print(f"{num} is a multiple of 4")
elif num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")


#break statement
num = int(input("Enter a number: "))
for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not a prime number")
        break
else:
    print(f"{num} is a prime number")


#continue statement
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
    