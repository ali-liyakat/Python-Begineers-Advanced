import numpy as np

rev_q1 = np.array([10, 12, 9])
print(rev_q1)
print(rev_q1.ndim)

rev = np.array([[10, 12, 9], [15,11, 13]])
print(rev)
print(rev.ndim)

print(rev[1,1])

rev[1,2] = 14
print(rev)
print(rev.dtype)

rev1 = np.array([10, 12, 9], dtype=np.float64)
print(rev1)
print(rev1.itemsize)
print(rev1.shape)
print(rev1.size)

# sort the array
rev2 = np.array([[10, 12, 9], [15,11, 13]])
print(rev2)
rev2.sort()
print(rev2)
sorted_array = np.sort(rev2, axis=None)
print(sorted_array)

# zeros
zeros = np.zeros((3,4))
print(zeros)

# ones
ones = np.ones((3,4))
print(ones)

# arange    
arrange = np.arange(1, 5)
print(arrange)

# linspace
linspace = np.linspace(1, 5, 10)
print(linspace)


# ravel: modifies the original array
rev = np.array([[10, 12, 9], [15, 11, 13]])
print(rev.ravel())


# flatten: returns a new array
print(rev.flatten())

# Reshape
rev = np.array([[10, 12, 9], [15, 11, 13]])
print(rev)
print(rev.reshape(3,2))


print(rev.min())
print(rev.max())

print(rev.sum(axis=0))
print(rev.sum(axis=1))

# for loops
for row in rev:
    print(f"Row is ->: {row}")

my_array = np.array([1, 4, 9])
print(np.sqrt(my_array))
print(np.square(my_array))