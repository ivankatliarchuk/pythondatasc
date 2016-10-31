# asymptotic analysis
data = [int(input()) for _ in range(int(input()))]



import math

def isPrime(number):
    root = int(math.sqrt(float(number)))
    if number == 1:
        return False
    for val in range(root):
        if val > 1 and number % val == 0:
            return False
    return True
def isPrimeV2(num):
    if num == 1:
        return "Not prime"
    sq = int(math.sqrt(num))
    for x in range(2, sq+1):
        if num % x == 0:
            return "Not prime"
    return "Prime"

for number in data:
    print(isPrimeV2(number))



'''
30
1
4
9
16
25
36
49
64
81
100
121
144
169
196
225
256
289
324
361
400
441
484
529
576
625
676
729
784
841
907
'''

'''
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Prime
'''
