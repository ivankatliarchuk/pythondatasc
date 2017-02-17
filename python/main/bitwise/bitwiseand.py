'''

When k is ODD , k-1 is EVEN , k-1 can always be reached by (k-1) & k.
In binary form:
    k   = 11
    k-1 = 10
    k-1 == (k-1) & k

  That is , ((k-1) | k) is always k. And ((k-1) | k) <= n is always TRUE.

In binary form:
    k   = 10110
    k-1 = 10101
    pos = 10111
    k-1 == (k-1) & pos

You can get k-1 if pos <= n is TRUE. And you can get pos by ((k-1) | (k-1+1)) , that is , ((k-1) | k).
 Otherwise , you just need to follow the process above when k is ODD (because k-1 is ODD) , then you get the answer k-2.

In brief , you can just do the test ((k-1) | k) <= n to determine the answer.
'''


def testValue(number, constant):
    num = 1
    max = 0
    while num in range(number):
        z = num + 1
        while z in range(number + 1):
            current = num & z
            if current < constant and current > max:
                max = current
            z += 1
        num += 1
    return max


t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    print(testValue(n, k))

'''
Objective
Welcome to the last day! Today, we're discussing bitwise operations. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given set . Find two integers,  and  (where ), from set  such that the value of  is the maximum possible and also less than a given integer, . In this case,  represents the bitwise AND operator.

Input Format

The first line contains an integer, , the number of test cases.
Each of the  subsequent lines defines a test case as  space-separated integers,  and , respectively.

For each test case, print the maximum possible value of  on a new line.

Sample Input

3
5 2
8 5
2 2
Sample Output

1
4
0
'''
