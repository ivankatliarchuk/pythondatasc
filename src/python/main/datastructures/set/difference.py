int(input())
first = set(map(int, input().split()))
int(input())
second = set(map(int, input().split()))

print(len(first.difference(second)))