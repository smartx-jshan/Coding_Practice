#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    index = 0
    space = " "
    staircase = "#"
    for i in range (1,n+1):
        temp = ""
        for j in range (1,n-i+1):
            temp = temp + space
        for k in range (1, i+1):
            temp = temp + staircase
        print (temp)

        
        
    
if __name__ == '__main__':
    n = int(input())

    staircase(n)

