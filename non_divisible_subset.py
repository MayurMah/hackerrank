#!/bin/python3

import math
import os
import random
import re
import sys
from operator import add


# Complete the nonDivisibleSubset function below.
def nonDivisibleSubset(k, S):
    temp = [0] * k

    for x in S:
        temp[x % k] += 1

    res = 0

    for i in range(k // 2 + 1):
        if i == 0 or k == i * 2:
            res += bool(temp[i])
        else:
            res += max(temp[i], temp[k - i])

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    S = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, S)

    fptr.write(str(result) + '\n')

    fptr.close()
