int(input())
first = set(map(int, input().split()))
int(input())
second = set(map(int, input().split()))

#  first ^ second
print(len(first.symmetric_difference(second)))
print(len(first ^ second))