"""
TASK
You a given a string S. You task is to swap cases in other words, convert all lowercase letters to uppercase
letters and vice versa.
INPUT
A single line containing a string S
CONSTANTS
0 < len(S) <= 1000
OUTPUT
Print the modified string S
SAMPLE INPUT
HackerRank.com presents "Pythonist 2".
SAMPLE OUTPUT
hACKERrANK.COM PRESENTS "pYTHONIST 2".
EXPLANATION
-----
"""
line = (input().strip())

def swap_case(s):
    swapped = ""
    for n in s:
        if n.isupper():
            swapped += n.lower()
        else:
            swapped += n.upper()
    return swapped

print(swap_case(line))
print(line.swapcase())


import sys

for line in sys.stdin:
    #line = line[:-1]
    line = ''.join([c.upper() if c.islower() else c.lower() for c in line])
    print(line)
