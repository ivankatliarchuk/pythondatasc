import calendar

def analytics(M, D, Y):
    return calendar.day_name[calendar.weekday(Y, M, D)].upper()

if __name__ == '__main__':
    Month, Day, Year = list(map(int, input().split()))
    print(analytics(Month, Day, Year))
