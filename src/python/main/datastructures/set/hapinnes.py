input().split()
first = list(map(int, input().split()))
happy = set(map(int, input().split()))
grumpy = set(map(int, input().split()))

print(sum([(i in happy) - (i in grumpy) for i in first]))
