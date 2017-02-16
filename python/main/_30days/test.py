
import math

for val in range(841):
    if val > 1 and 841 % val == 0:
       print(val)

def isPrime(number):
    root = int(math.sqrt(float(number)))
    if number == 1:
        return False
    for val in range(root):
        if val > 1 and number % val == 0:
            return False
    return True

def isPrime2(num):
    if num == 1:
        return "Not prime"
    sq = int(math.sqrt(num))
    for x in range(2, sq+1):
        if num % x == 0:
            return "Not prime"
    return "Prime"

print(str(isPrime(841)))
