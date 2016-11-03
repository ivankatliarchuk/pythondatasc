'''
We can generate the transposition of an array using the tool numpy.transpose.
It will not affect the original array, but it will create a new array.

my_array = np.array([1,2,3], [4,5,6])
np.transpose(my_array)
'''

'''
Flatten
my_array = np.array([1,2,3], [4,5,6])
my_array.flatten()
'''

'''
Task:
You are given a X integer array matrix with space separated elements ( = rows and  = columns).
Your task is to print the transpose and flatten results.

Input Format

The first line contains the space separated values of  and .
The next  lines contains the space separated elements of  columns.

Output Format

First, print the transpose array and then print the flatten.

Input
2 2
1 2
3 4

output

[[1 3]
 [2 4]]
[1 2 3 4
'''

# array = []
# for num in range([int(a_temp) for a_temp in input().strip().split(' ')][0]):
#      data = [int(a_temp) for a_temp in input().strip().split(' ')]
#      array.append(data)
#
# tr_array = np.transpose(np.array(array))
# print(tr_array)
# print(np.array(array).flatten())

lista = [list(map(int, input().split())) for i in range([int(a_temp) for a_temp in input().strip().split(' ')][0])]

print(lista)
