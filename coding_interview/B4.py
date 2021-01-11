#0 < n <= 10
#0 < t <= 60
#0 < m <= 45
from typing import List

# HH:MM
def solution (n: int, t: int, m: int, timetable: List[str] ) -> str:
    timetable = [ int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    timetable.sort()
    #print (timetable)

    current = 540

    for n in range (n):
        for _ in range (m):
            if timetable and timetable[0] <= current:
                candidate = timetable.pop(0) -1
            else:
                candidate = current

        current += t

    h, m = divmod(candidate, 60)
    return str(h).zfill(2) + ":" +str(m).zfill(2)

n = 1
t = 1
m = 5
table1= ["08:00", "08:01", "08:02", "08:03"]

n2 = 10
t2 = 60
m2 = 45
table2= ["23:59"]
print (solution(n2, t2, m2, table2))

