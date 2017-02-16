from collections import defaultdict

d = defaultdict(list)
d['python'].append('awesome')
d['something-else'].append('not relevant')
d['python'].append('language')

print(d)


for d in d.items():
    print(d)
