import datetime
from typing import List


def solution (lines: List[str]) -> int:
    #print (lines)

    combined_logs = []
    for line in lines:
        logs = line.split(' ')
        #print (logs)
        timestamp = datetime.datetime.strptime(logs[0] + ' ' + logs[1], "%Y-%m-%d %H:%M:%S.%f").timestamp()
        #print (timestamp)
        combined_logs.append((timestamp, -1))
        combined_logs.append((timestamp - float(logs[2][:-1]) + 0.001, 1))
        #print (combined_logs)
    #print (combined_logs)
    accumulated = 0
    max_request = 1
    combined_logs.sort(key=lambda x: x[0])
    #print (combined_logs)

    for i, elem1 in enumerate(combined_logs):
        current = accumulated

        for elem2 in combined_logs[i:]:
            if elem2[0] - elem1[0] > 0.999:
                break
            if elem2[1] > 0:
                current += elem2[1]

        max_request = max(max_request, current)
        accumulated+= elem1[1]

    return max_request

lines = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]

print (solution (lines))
