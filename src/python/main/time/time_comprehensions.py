import timeit

keys = ('name', 'age', 'food')
values = ('Monty', 42, 'spam')

min(timeit.repeat(lambda: {k: v for k, v in zip(keys, values)}))
min(timeit.repeat(lambda: dict(zip(keys, values))))
min(timeit.repeat(lambda: {keys[i]: values[i] for i in range(len(keys))}))
min(timeit.repeat(lambda: dict([(k, v) for k, v in zip(keys, values)])))
min(timeit.repeat(lambda: dict((k, v) for k, v in zip(keys, values))))
