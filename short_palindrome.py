#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the shortPalindrome function below.
def shortPalindrome(s):
    """Find number of short palindromes in input string s using dynamic programming

    Args:
        s(str): input string

    Returns:
        Number of short palindromes in the input string (int)

    """

    if len(s) < 1:
        return 0

    s_len = len(s)
    num_alpha = 26
    MOD = 10 ** 9 + 7

    ans = 0
    c1 = [0 for i in range(num_alpha)]
    c2 = [[0 for i in range(num_alpha)] for j in range(num_alpha)]
    c3 = [[0 for i in range(num_alpha)] for j in range(num_alpha)]

    for current in s:
        c = ord(current) - ord('a')
        for i in range(26):
            ans += (c3[c][i] % MOD)
            c3[i][c] += c2[i][c]
            c2[i][c] += c1[i]
        # print(c, c1[i], c2[i][c], c3[c][i])
        c1[c] += 1

    return ans % MOD


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = shortPalindrome(s)

    fptr.write(str(result) + '\n')

    fptr.close()
