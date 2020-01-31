#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    row=0
    col=0
    curmax=hoursum([x[0:3] for x in arr[0:3]])
    for row in range(4):
        for col in range(4):
            curmax= max(curmax,hoursum([x[col:col+3] for x in arr[row:row+3]]))
            #print(curmax)
    return curmax

def hoursum(arr):
    return (sum(arr[0])+arr[1][1]+sum(arr[2]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
