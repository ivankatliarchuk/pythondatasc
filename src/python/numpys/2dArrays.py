import numpy as np

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([64.4, 59.2, 63.6, 88.4, 68.7])

print(type(np_height))

data = np.array([[1.73, 1.68, 1.71, 1.89,1.79],
                [65.4, 59.2, 63.6, 88.4, 68.7]])

print(data[0,2]) # first row 2 elements
print(data[:,1:3]) # each row, get only from 1 to 3
print(data[1,:]) # print second row
