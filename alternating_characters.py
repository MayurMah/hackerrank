#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    """Find minimum number of deletions required to delete all consecutive repeating characters from the given string.
        Ex. AABAAB -> ABAB (ans: 2)

    Args:
        s(str): given string

    Returns:
        Minimum number of deletions required to delete all consecutive repeating characters from the given string.

    """

    return sum([s[i:i + 2] in {'AA', 'BB'} for i in range(len(s))])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
