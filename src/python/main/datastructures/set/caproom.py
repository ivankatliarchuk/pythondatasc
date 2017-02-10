N = int(input())
data = list(map(int, input().split()))

rooms = {}

for num in data:
    if rooms.get(num) is None:
        rooms[num] = 1
    else:
        rooms[num] += 1

for r in rooms:
    if rooms[r] != N:
        print(r)
        break
