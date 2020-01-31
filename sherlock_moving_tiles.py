#!/bin/python3

import os
import sys
import math
#
# Complete the movingTiles function below.
#
def movingTiles(l, s1, s2, queries):
    #

    if s1>s2:
        s_hi = s1
        s_lo = s2
    else:
        s_hi = s2
        s_lo = s1
    #print(l,s_hi,s_lo,queries)
    t = [0]*len(queries)
    for i,q in enumerate(queries):
        t[i] = math.sqrt(2)*(l-math.sqrt(q))/(s_hi-s_lo)
    #print(t)
    return t
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lS1S2 = input().split()

    l = int(lS1S2[0])

    s1 = int(lS1S2[1])

    s2 = int(lS1S2[2])

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = movingTiles(l, s1, s2, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
