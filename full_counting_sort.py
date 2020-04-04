#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


# Complete the countSort function below.
def countSort(arr):
    n = len(arr)
    num_list = [[] for i in range(n)]

    for i in range(n):
        key = int(arr[i][0])
        val = arr[i][1]
        if i < n // 2:
            val = '-'
        num_list[key].append(val)

    result = ' '.join([' '.join(x) for x in num_list if len(x) > 0])
    print(result)


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
