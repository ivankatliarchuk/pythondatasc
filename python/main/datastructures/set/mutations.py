N = int(input())
superset = set([int(x) for x in input().split()])

NN = int(input())
for num in range(NN):
    command, length = input().split()
    data= set([int(x) for x in input().split()])
    if command == 'intersection_update':
        superset.intersection_update(data)
    elif command == 'update':
        superset.update(data)
    elif command == "symmetric_difference_update":
        superset.symmetric_difference_update(data)
    else:
        superset.difference_update(data)

print(sum(superset))
