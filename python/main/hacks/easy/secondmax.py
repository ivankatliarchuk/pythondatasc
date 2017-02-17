
n = int(input().strip())
number = list(map(int, input().strip().split(' ')))

maximum = max(number)
prevMax = -100000000
for num in number:
    if prevMax < num and maximum > num:
        prevMax = num

print(prevMax)



