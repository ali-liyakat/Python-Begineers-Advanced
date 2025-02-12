#  List contains elements of different data type
# store sequence of elements in order
# they are mutable



items = ['bread', 'pasta', 'cheese', 'veggies', 'butter']
print(items)
print(items[0])     # lists are 0 indexed

print(items[0:2])   # slicing

items.append('rice')    # append to end of list
print(items)

items.remove('rice')   # remove element from list
print(items)

items.insert(0, 'rice')    # insert element at index
print(items)

items[0] = 'roti'   # update element at index
print(items)

print(len(items))   # length of list

print('bread' in items)   # check if element is in list



expenses = [26800, 2350, 2600, 21130, 2190, 300]
expenses.sort()    # sort list inplace Ascending order
print(expenses)

expenses.sort(reverse=True)    # sort list inplace Descending order
print(expenses)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)
print(dir(list3))    # list of methods available for list

list3.clear()    # clear list
print(list3)

random_list = ['a', 1, 2, 'b', 'c', 3]
print(random_list)