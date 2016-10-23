
stocks = { "GOOG": (613.30, 625.86, 610.50),
           'MSFT': (30.25, 30.70, 30.19)}

print(stocks['GOOG'])
print(stocks.get('MSFT'))
print(stocks.get('RIM', 'NOT FOUND'))

stocks.setdefault('RIM', (67.34, 68.48, 67.28))


for stock, values in stocks.items():
    print("{} last value is {}".format(stock, values[-1]))
