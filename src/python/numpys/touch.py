height = [1.73, 1.68, 1.71, 1.89, 1.79]

weigh = [65.4, 59.2, 63.6, 88.4, 68.7]

import numpy as np
np_height = np.array(height)
np_weight = np.array(weigh)

bmi = np_weight / np_height ** 2
print(bmi)
print(bmi > 22)
print(bmi[bmi > 23]) # only show with bmi > 23. lol so coool
