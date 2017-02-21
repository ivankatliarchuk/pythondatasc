import calendar
from datetime import timedelta
from datetime import datetime
import time
format = '%a %d %b %Y %H:%M:%S %z'

def analytics():
    return -1

if __name__ == '__main__':
    S = str(input().strip())
    S2 = str(input().strip())
    date = datetime.strptime(S, format)
    another = date.timestamp()
    d2 = datetime.strptime(S2, '%a %d %b %Y %H:%M:%S %z')
    a2 = date.timestamp()
    print(another)
    print(a2)
    '''
    Sun 10 May 2015 13:54:36 -0700
    Sun 10 May 2015 13:54:36 +0000
    '''
   # print(date)
    print(int(another - a2))
    #print(timedelta.resolution(date, another))
    # Day dd Mon yyyy hh:mm:ss +xxxx
    # N = int(input().strip())
    # for num in range(N):
    #     data = list(map(str, input().split()))
    #     print(analytics(data[1], data[2], data[3], data[4], data[5]))
