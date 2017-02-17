superset = set([int(x) for x in input().split()])
N = int(input())

result = True
for num in range(N):
    data = set([int(x) for x in input().split()])
    result = superset.issuperset(data)
    if result == False:
        break

print(result)
