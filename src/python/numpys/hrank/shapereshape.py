'''
shape and reshape arrays
'''

import numpy as np

array = np.array([[1, 2],[3, 4],[6,5]])
sec_array = np.array([1, 2, 3, 4, 5, 6])
sec_array.shape = (3, 2)
print(sec_array)

'''
reshape
'''

array_v2 = np.array([1, 2, 3, 4, 5, 6])
print(np.reshape(array_v2, (3, 2)))

my_array = np.array([1,2,3,4,5,6])
print(np.reshape(my_array,(3,2)))


arr_v1 = np.reshape(np.array([int(a_temp) for a_temp in input().strip().split(' ')]), (3, 3))
print(arr_v1)
