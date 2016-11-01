n = int(input().strip())
a = list(map(int, input().strip().split(' ')))


marksheet = [[input(), float(input())] for _ in range(n)]

a = [int(a_temp) for a_temp in input().strip().split(' ')]

'''
return dictionary
'''
dictionary = dict([(input().split(' ')) for _ in range(n)])
