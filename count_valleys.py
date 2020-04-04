#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    steps = [1 if c == "U" else -1 for c in s]

    level = 0
    nvalleys = 0
    insidevalley = 0

    for step in steps:
        level += step
        if (level == 0):
            insidevalley = 0
        if (level < 0 and insidevalley == 0):
            insidevalley = 1
            nvalleys += 1
    return nvalleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
