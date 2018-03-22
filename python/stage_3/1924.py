from calendar import weekday

day=['MON','TUE','WED','THU','FRI','SAT','SUN']
date= weekday(2007,*map(int,input().split()))
print (day[date])
