from collections import Counter

c = Counter('which')
print(c)
c.subtract('witch')
print(c)

nums = Counter([1, 4, 6, 4, 5, 9, 0, 4, 5])
print(nums)
nums.subtract([1])
print(nums)
nums.subtract([1])
print(nums)
nums.pop(1)
print(nums)
