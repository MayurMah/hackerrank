#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the lilysHomework function below.
def numSwaps(arr):
    positions = sorted(list(enumerate(arr)), key=lambda e: e[1])
    num_swaps = 0
    swapped_idx = 0

    for idx in range(len(arr)):
        while True:
            if idx == positions[idx][0]:
                break
            else:
                num_swaps += 1
                swapped_idx = positions[idx][0]
                positions[idx], positions[swapped_idx] = positions[swapped_idx], positions[idx]
    return num_swaps


def lilysHomework(arr):
    """Find the number of swaps needed to get to an array where difference between consecutive elements is minimum

    Args:
        arr(list): input list of integers

    Returns:
        Number of swaps needed (int)

    """

    return min(numSwaps(arr), numSwaps(arr[::-1]))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
