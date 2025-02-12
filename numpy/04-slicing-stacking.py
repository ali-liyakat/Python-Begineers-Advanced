import numpy as np

a = np.array([1, 2, 3, 4])
print(a[0:3])


b = np.array([[1, 2, 3],
              [4,5, 6],
              [7, 8, 9]])
print(b[1, 2])
print(b[1, 1:3])


# customer ID, name
cust = np.array([[101, 'Mira'],
                 [102, 'Ali'],
                 [103, 'Raj']])

# customer ID, amout, date
dat = np.array([[101, 200, '10-09-2023'],
                [102, 400, '10-12-2024'],
                [103, 600, '10-06-2022']])


h_merged = np.hstack((cust, dat))
print(h_merged)

e = np.array([[201, 'Bob'],
              [202, 'Mary'],
              [203, 'winn']])
print(np.vstack((cust, e)))


# hsplit
x, y = np.hsplit(h_merged, [2]) # splits at column 3
print(x)
print(y)

# vsplit
s, t= np.vsplit(h_merged, [1]) # splits at column
print(s)
print(t)


monthly_sales = np.array([30, 36, 32, 39, 29, 37])
res = monthly_sales < 32
print(res)
print(monthly_sales[res])

print(np.argmax(monthly_sales)) # index of maximum element


