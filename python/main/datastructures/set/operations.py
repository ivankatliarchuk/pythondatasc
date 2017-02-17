data =  set()
print(data)

# modifiying set

data.add('c')
data.add((4, 5))
print(data)
# update only works for iterable objects
data.update([1, 4, 6, 9])
data.update({3, 8}, {44, 12})
print(data)

# removing items
data.discard(12)
print(data)
# raise exception if not exists
data.remove(44)
print(data)
# common operations
a = {2, 4, 5, 9}
b = {2, 4, 11, 12}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))


