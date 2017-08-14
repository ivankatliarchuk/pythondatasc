#!/usr/bin/env python

def counter():
    i = 0
    while True:
        i +=1
        yield i

a = counter()

print next(a)
print next(a)
print next(a)
