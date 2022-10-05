import datetime

def solution():
    today = input()
    d = datetime.datetime.strptime(today, '%B %d, %Y %H:%M')
    d2 = datetime.datetime(d.year, 1, 1, 0, 0)
    td = d - d2
    totalSecond = td.total_seconds()

    if ((d.year%4 == 0)and(d.year%100!=0))or(d.year%400==0):
        print((totalSecond/31622400)*100)
    else:
        print((totalSecond/31536000)*100)
    

solution()