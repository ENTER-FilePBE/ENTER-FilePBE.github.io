# this is for generating input.csv, to convert it to output.csv automatically, see com.sissel.file.util.

from datetime import datetime, timedelta
import random

begin = datetime.strptime('2015-3-14', '%Y-%m-%d')
end = datetime.strptime('2017-8-25', '%Y-%m-%d')


def num2str(num):
    if num < 10:
        return '0' + str(num)
    else:
        return str(num)


if __name__ == '__main__':
    current = begin
    cnt = 0
    while current < end:
        dt = datetime.now()
        ri = random.randint(0, 9)
        cnt += 1

        # 10% not change, 60% +1day, 10% +2days, 10% +3days, 10% +4days
        if 0 < ri <= 6:
            current += timedelta(days=1)
        elif ri >= 7:
            current += timedelta(days=ri - 5)
        dt = dt.replace(year=current.year, month=current.month, day=current.day)
        yStr = num2str(dt.year)
        mStr = num2str(dt.month)
        dStr = num2str(dt.day)
        hStr = num2str(random.randint(0, 23))
        minStr = num2str(random.randint(0, 59))
        print('"IMG_', yStr, mStr, dStr, hStr, minStr, '"', end=',', sep='')
        print('"JPG",', '"",', '"', str(random.randint(200123, 433209)), '"', end=',', sep='')
        print('"', yStr, '-', mStr, '-', dStr, ' ', hStr, ':', minStr, ':00.000"', end=',', sep='')
        print('"false","false","false","false","', 'i', str(cnt), '"', sep='')
