import numpy as np
import sys


# Numpy arrays are memory efficient than python lists

my_list = [1, 2, 3, 4, 5]
print(sys.getsizeof(my_list[0])* len(my_list))  # 140


arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr.nbytes)   #40



# Access of elements in numpy arrays is faster than python lists

import time

SIZE = 1000000
l1 = list(range(SIZE))
l2 = list(range(SIZE))
start_time = time.time()
result = [(x+y) for x, y in zip(l1, l2)]
end_time = time.time()
print("Python list took: ", (end_time - start_time)*1000)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

start_time = time.time()
result = a1 + a2
end_time = time.time()
print("Numpy array took: ", (end_time - start_time)*1000)

# Convenient use of built-in functions

a1 = np.array([1, 2, 3, 4, 5])
a2 = np.array([6, 7, 8, 9, 10])

print(a1 + a2)
print(a1 * a2)