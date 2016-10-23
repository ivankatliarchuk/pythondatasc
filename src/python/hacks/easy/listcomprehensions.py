
x = 1
y = 1
z = 1
n = 2

values = [[f, s, t] for f in range(x + 1) for s in range(y + 1) for t in range(z + 1) if f + s + t != n]
print(values)


'''
second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))

'''
# my_dict = [(name, hero) for name in names for hero in heros]
