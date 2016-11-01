
# n = int(input().strip())
# data =  tuple(map(int, input().strip().split(' ')))
# print(data.__hash__())


from collections import namedtuple as ntup

Stock = ntup("Stock", "symbol current high low")
stock = Stock('GOOG', 613.30, high= 625.86, low= 610.50)
print(stock)
