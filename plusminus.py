#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p,n,z=0,0,0
    l  = len(arr)
    #print(arr,p,n,z)
    p = len([i for i in arr if i>0])
    n = len([i for i in arr if i<0])
    z = l-p-n
    p = p/l
    n = n/l
    z = z/l
    print("{0:.6f}".format(p))
    print("{0:.6f}".format(n))
    print("{0:.6f}".format(z))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
