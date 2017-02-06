"""
TASK
Compute the average of all the plants with distinct heights in her greenhouse
Average = (Sum of Disticnt Heights) / (Total number of Distinct heughts)
INPUT
The first line contains the integer, N, the total number of plants.
The second line contains the N space separated heights of the plants.
CONSTANTS
0 < N <= 100
OUTPUT
Output the average height value on a single line
SAMPLE INPUT
10
161 182 161 154 176 170 167 171 170 174
SAMPLE OUTPUT
169.375
EXPLANATION
-----
"""
def average(array):
    data = set(array)
    return sum(data) / len(data)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
