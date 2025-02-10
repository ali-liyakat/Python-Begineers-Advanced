# functions are code blocks for a particular task.
# Save from code repetition
# code modularity.


# function definition
def find_expenses(expenses):
    '''This function takes a list of expenses and returns the total expenses'''
    total = 0
    for expense in expenses:
        total += expense
    return total

# function call
toatl_alice = find_expenses([100, 200, 300])
print(toatl_alice)

# print docstring
# print(help(find_expenses))


#positional arguments
def volume_cylinder(radius, height):
    '''This function takes the radius and height of a cylinder and returns the volume'''
    volume = 3.14 * radius**2 * height
    return volume

# function call
volume = volume_cylinder(2, 5)
print(volume)

# keyword arguments
# volume of a cylinder
def volume_cylinder(radius, height):
    '''This function takes the radius and height of a cylinder and returns the volume'''
    volume = 3.14 * radius**2 * height
    return volume

# function call
volume = volume_cylinder(radius=2, height=5)
print(volume)

# default arguments
def volume_cylinder(radius, height=5):
    '''This function takes the radius and height of a cylinder and returns the volume'''
    volume = 3.14 * radius**2 * height
    return volume

# function call
volume = volume_cylinder(radius=2)
print(volume)

# variable-length arguments
def sum_all(*args):
    '''This function takes any number of arguments and returns the sum'''
    total = 0
    for arg in args:
        total += arg
    return total

# function call
print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# variable-length keyword arguments
def print_all(**kwargs):
    '''This function takes any number of keyword arguments and prints them'''
    for key, value in kwargs.items():
        print(key, value)

# function call
print_all(name='Alice', age=25, city='New York')
       

# lambda function
square = lambda x: x**2
print(square(5))


# pass keyword
def my_function():
    pass

# function call
my_function()


import math
# Built-in functions
my_list = [10, 20, 30, 40, 50]
print(sum(my_list))
print(max(my_list))
print(min(my_list))
print(math.sqrt(25))

