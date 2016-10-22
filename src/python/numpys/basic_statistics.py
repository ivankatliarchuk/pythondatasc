import numpy as np

np_city = np.array([[1.64, 71.78],
                    [1.37, 63.65],
                    [2.01, 73.57]])

average_height = np.mean(np_city[:,0])
print(average_height)

median_height = np.median(np_city[:,0])
print(median_height)

std_height = np.std(np_city[:,0])
print(std_height)

cooreleation_height = np.corrcoef(np_city[:,0], np_city[:,1])
print(cooreleation_height)

# generate data
height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)
np_city = np.column_stack((height, weight)) # tuple inside of the brackets
print(np_city)

