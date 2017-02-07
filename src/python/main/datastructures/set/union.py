"""
TASK
The students of District College have subscriptions to English and French newspapers. Some students have
subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.

You are given two sets of student roll number. One set has subscribed to the English newspaper, and the other
set is subscribed to the French newspaper. The same studend could be in both sets. You task is to find the total
number of students who have subscribed to at least one newspaper.
INPUT
The first line contains an integer, n, the number of students who have subscribed to the English newspaper.
The second line contains n space separated roll numbers of those students.
The third line contains b, the number of students who have subscribed to the French newspaper.
The fourth line contains b space separated roll numbers of those students.
CONSTANTS
0 < Total number of students in college < 1000
OUTPUT
Output the total number of students who have at least one subscription
SAMPLE INPUT
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
SAMPLE OUTPUT
13
EXPLANATION
Roll numbers of students who have at least one subscription:
1,2,3,4,5,6,7,8,9,10,11,21 and 55. Roll numbers: 1,2,3,6 and 8 are in both sets so they are only counted once.
Hence, the total is  students.
"""
int(input())
english = set(map(int, input().split()))
int(input())
french = set(map(int, input().split()))

# can use union
print(len(english | french))
