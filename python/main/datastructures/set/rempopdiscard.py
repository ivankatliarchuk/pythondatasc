"""
TASK
Have a non empty set, and you have to execute N commands given N times.
The command will be pop, remove and discard.
INPUT
The first line contains integer n, the number of elements in the set a.
The second line contains n space separated elements of set s. All of the elements are non-negative integers, less
that or equal to 9.
CONSTANTS
0 < n < 20
0 < N < 20
OUTPUT
Print the sum of the elements of set s on a single line.
SAMPLE INPUT
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5
SAMPLE OUTPUT
4
EXPLANATION
-----
"""
n = int(input())
data = set(map(int, input().split()))

N = int(input())
for i in range(N):
    line = list(input().split())
    if line[0] == 'pop':
        data.pop()
    elif line[0] == 'remove':
        data.remove(int(line[1]))
    elif line[0] == 'discard':
        data.discard(int(line[1]))

print(sum(data))

