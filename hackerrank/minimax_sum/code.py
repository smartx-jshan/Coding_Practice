#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    index =0
    a = []
    sum = 0 
    for j in arr:
        sum = sum + j
    
    for i in range (0,5):
        a.append(sum - arr[index])
        index = index + 1
    minValue = min (a)
    maxValue = max (a)
    print (minValue, maxValue)
        

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

