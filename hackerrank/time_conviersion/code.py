#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if ("PM" in s):
        s= s.rstrip("PM")
        time = int(s[0:2])
        time = time + 12
        if (time == 24):
            time = 12
        s = s[2:]
        s = str(time) + s
    else:
        s= s.rstrip("AM")
        time = int(s[0:2])
        if (time == 12):
            s = s[2:]
            s = "00" + s 
    return s

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

