
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(a_temp) for a_temp in input().strip().split(' ')]

def library(rent, returned):
    if rent[2] == returned[2]:
        if rent[1] == returned[1]:
            if rent[0] <= returned[0]:
                return 0
            else:
                delay = abs(rent[0] - returned[0])
                return delay * 15
        elif rent[1] < returned[1]:
            delay = abs(rent[1] - returned[1])
            return delay * 500
        else:
            return 0
    elif rent[2] < returned[2]:
        return 10000
    return 0

print(int(library(a, b)))

rd, rm, ry = [int(x) for x in input().split(' ')]
ed, em, ey = [int(x) for x in input().split(' ')]

if (ry, rm, rd) <= (ey, em, ed):
    print(0)
elif (ry, rm) == (ey, em):
    print(15 * (rd - ed))
elif ry == ey:
    print(500 * (rm - em))
else:
    print(10000)


'''
9 6 2015
6 6 2015
45
----
8 6 2015
9 6 2015
0
----
8 6 2015
9 6 2016
10000
-----
8 3 2015
9 6 2015
1500

test
2 6 2014
5 7 2014
0

1 1 2010
31 12 2009
10000
'''
