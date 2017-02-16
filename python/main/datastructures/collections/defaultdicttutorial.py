from collections import defaultdict

d = defaultdict(list)

N,M = (map(int, input().strip().split(' ')))

for n in range(N):
    d['A'].append(input().strip())


for m in range(M):
    d['B'].append(input().strip())


print(d)

