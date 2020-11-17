#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    
    size = len(arr)
    positive = 0
    negative = 0
    zeros = 0
    for i in arr:
        if (i > 0):
            positive = positive + 1
        elif (i == 0):
            zeros = zeros + 1
        else:
            negative = negative + 1
    
    print (round(positive/size,6))
    print (round(negative/size,6))
    print (round(zeros/size,6))
        

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

