'''
generate array transposition
'''

import numpy as np

arr_v1 = np.array([[1, 2, 3],
                   [4, 5, 6]])

print(np.transpose(arr_v1))

'''
flatten array to one dimension
'''
arr_v2 = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(arr_v2.flatten())
