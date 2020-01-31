#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    prev_lcs = [0] * (len(s2) + 1)
    cur_lcs = [0] * (len(s2) + 1)
    for c1 in s1:
        cur_lcs, prev_lcs = prev_lcs, cur_lcs
        for i, c2 in enumerate(s2, 1):
            if c1 == c2:
                cur_lcs[i] = 1 + prev_lcs[i - 1]
            else:
                cur_lcs[i] = max(prev_lcs[i], cur_lcs[i - 1])
    return cur_lcs[-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
