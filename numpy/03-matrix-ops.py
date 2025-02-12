import numpy as np

q1 = np.array([[200,220,250],[210,230,270],[190,210,250]])

q2 = np.array([[209, 230, 190], [220, 240, 270], [200, 220, 250]])

print(q1 + q2)
print(q1 - q2)


prices = np.array([[200,300, 360],[390, 400,260], [190, 240, 270]])

q1_rev = q1 * prices
print(q1_rev)

q1_discount = q1 * 0.3
print(q1_discount)

net_rev = q1_rev - q1_discount
print(net_rev)

print(np.sum(net_rev))


features = np.array([[30000, 4],[10000, 2]])
weights = np.array([150, 40000])

print(np.dot(features,weights))


c   = np.array([1, 2,3])
d = np.array([4,5,6])
print(np.cross(c,d))


# transpose the matrix
matrixx = np.array([[1,2,3],[4,5,6]])
print(matrixx.transpose())