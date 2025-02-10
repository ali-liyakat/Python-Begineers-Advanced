# for loop
# definte Loop: for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects. Iterating over a sequence is called traversal.

expenses = [26800, 2350, 2600, 21130, 2190, 300]
total = 0
for expense in expenses:
    total += expense
print(f"Total expenses: {total}")


# range() function: range() function is used to generate a sequence of numbers. It is commonly used in for loop.
expenses = [26800, 2350, 2600, 21130, 2190, 300]
months = len(expenses)
for month in range(months):
    print(f"Month {month + 1} expenses: {expenses[month]}")
print(f"Total expenses: {sum(expenses)}")


# enumerate() function: enumerate() function is used to loop over an iterable object and provide an automatic counter.
expenses = [26800, 2350, 2600, 21130, 2190, 300]
for i, expense in enumerate(expenses):
    print(f"Month {i + 1} expenses: {expense}")
print(f"Total expenses: {sum(expenses)}")


# break statement: break statement is used to exit the loop.
sales = [100, 600, 300, 400, 500, 200]
target = 200
for sale in sales:
    if sale == target:
        print(f"Target achieved: {sale} at index {sales.index(sale)}")
        break
    print(f"Sale: {sale}")


# zip() function: zip() function is used to combine two or more iterables. It returns an iterator of tuples.
sales = [100, 600, 300, 400, 500, 200]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
for month, sale in zip(months, sales):
    print(f"{month} sale: {sale}")


# continue statement: continue statement is used to skip the current iteration and continue with the next iteration.
sales = [700, 600, 40, 300, 400, 500, 200, 50, 80]
target = 200
for sale in sales:
    if sale < target:
        continue
    print(f"Sale: {sale}")


# while loop: while loop is used to execute a block of code repeatedly as long as the condition is true.
sales = [100, 600, 300, 400, 500, 200]
target = 200
i = 0
while sales[i] != target:
    print(f"Sale: {sales[i]}")
    i += 1

# for else: for loop can have an optional else block which is executed when the loop completes normally (without break).
for i in range(7):
    print(i)
else:
    print("Loop completed normally")
