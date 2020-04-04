#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the larrysArray function below.
def rotate(a):
    a_min = min(a)
    if a_min == a[1]:
        return [a[1], a[2], a[0]]
    elif a_min == a[2]:
        return [a[2], a[0], a[1]]
    else:
        return a


def larrysArray(A):
    result = "NO"

    """i = 0
    A_sorted = sorted(A)
    while i < len(A) and A != A_sorted:
        # print(i,A)
        if i!=0 and A[i] < A[i-1]:
            if i != len(A)-1:
                # print("before",A[i-1:i+2])
                A[i-1:i+2] = rotate(A[i-1:i+2])
                # print("after",A[i-1:i+2])
            else:
                # print("before",A[i-2:])
                before = A[i-2:].copy()
                A[i-2:] = rotate(A[i-2:])
                if A[i-2:]==before:
                    break
                # print("after",A[i-2:])
            i = 0
        else:
            i += 1
    if A == A_sorted:
        result = "YES"
    """

    print("cp1", A)

    inversions = 0
    seen = set()

    for i, a in enumerate(A):
        for s in seen:
            if a < s:
                inversions += 1
        seen.add(a)

    return "YES" if inversions % 2 == 0 else "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
