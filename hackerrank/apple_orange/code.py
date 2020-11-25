#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    app = []
    app_count = 0
    ora_count = 0
    
    for i in apples:
        temp = a + i
        if (temp in range(s,t+1)):
            app_count = app_count + 1
    
    for j in oranges:
        temp = b + j
        if (temp in range (s,t+1)):
            ora_count = ora_count + 1
    
    print (app_count)
    print (ora_count)
        

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

