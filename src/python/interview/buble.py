n = int(input().strip())
a = list(map(int, input().strip().split(' ')))


def sort(colection):
    ''''iterate over a collection of objects'''
    numberOfSwaps = 0
    idx = 0
    while idx < len(colection):
        inner = idx + 1
        while inner < len(colection):
            first = colection[idx]
            second = colection[inner]
            if (first > second):
                temp = first
                colection[idx] = colection[inner]
                colection[inner] = temp
                numberOfSwaps += 1
                inner += 1
            else:
                inner += 1
        idx += 1

    print(('Array is sorted in {} swaps.').format(numberOfSwaps))
    print(('First Element: {}').format(colection[0]))
    print(('Last Element: {}').format(colection[-1]))

sort(a)

'''
3
0 -89 3 67 -1 2

3
1 -2 2 3 -89
'''
