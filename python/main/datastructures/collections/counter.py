from collections import Counter

int(input().strip())
a = list(map(int, input().strip().split(' ')))
data = Counter(a)

amount = 0

N = int(input().strip())
for num in range(N):
    size, price = list(map(int, input().strip().split(' ')))
    value = data[size]
    # if size in S and S[size] > 0:
    # S[size] -= 1
    # earnings += x_i
    if value >= 2:
        data.subtract([size])
        amount += price
    elif value == 1:
        data.pop(size)
        amount += price

print(amount)
