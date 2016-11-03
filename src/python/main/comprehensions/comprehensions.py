x = 1
y = 1
z = 1
n = 2

values = [[f, s, t] for f in range(x + 1) for s in range(y + 1) for t in range(z + 1) if f + s + t != n]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# using a map + lambda
my_list = map(lambda n: n * n, nums)

print(my_list)

my_list = [n for n in nums]
print(my_list)

# i want n * n
my_list = [n * n for n in nums]
print(my_list)

# if 'n' is even
my_list = [n for n in nums if n % 2 == 0]
print(my_list)

# usinf a filter and a lambda
my_list = filter(lambda n: n % 2 == 0, nums)
print(list(my_list))

my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))
print(my_list)
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)

# dictionary comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# print(list(zip(names, heros)))

my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print(my_dict)
# all combinations
my_dict = [(name, hero) for name in names for hero in heros if name != 'Peter']
print(my_dict)
#  correspond to line 38-40
my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Bruce'}
print(my_dict)

# SET comprehensions
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
my_set = set()
for n in nums:
    my_set.add(n)

print(my_set)

my_set = set([n for n in nums])  # or {n for n in names}
print(my_set)

dd = [[].append(arr) for num in range([int(a_temp) for a_temp in input().strip().split(' ')].pop()) for (arr) in array for array in
      input().strip().split(' ')]
