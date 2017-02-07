"""
TASK
Given 2 sets of integers, M and N, print their difference in ascending order. The term symmetric
difference indicates values that exist in eirhter M or N but do not exist in both.
INPUT
The first line of input contains integer M.
The second line containts M space separeted integers.
The third line contains an integer N
The fourth line contains N space separated integers.
CONSTANTS
-----
OUTPUT
Output the symmetric difference integers an ascending order, one per line
SAMPLE INPUT
4
2 4 5 9
4
2 4 11 12
SAMPLE OUTPUT
5
9
11
12
EXPLANATION
-----
"""
M = int(input())
MM = set([int(x) for x in input().split()])
N = int(input())
NN = set([int(x) for x in input().split()])


difference = MM.symmetric_difference(NN)
data = list(difference)
data.sort()

# sorted(list)
for x in data:
    print(x)














