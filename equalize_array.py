#!/bin/python

import math
import os
import random
import re
import sys


# Complete the equalizeArray function below.
def equalizeArray(arr):
    return len(arr) - arr.count(max(arr, key=arr.count))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
