#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    a_sorted = sorted(arr)
    print(sum(a_sorted[:4]), sum(a_sorted[1:]))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
