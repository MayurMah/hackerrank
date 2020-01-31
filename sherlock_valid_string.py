#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):

    #print(s)

    if(len(s)==1):
        return "YES"

    c = Counter(s)
    vcount = 0
    vmin = min([i for i in c.values() if i>1])

    for k,v in c.items():
        if v ==vmin:
            continue
        else:
            vcount += abs(v-vmin)

    #print(vmin)
    #print(c.items())
    #print(vcount)

    if(vcount>1):
        if(len(set(c.values()))==2 and list(c.values()).count(1)==1):
            return "YES"
        else:
            return "NO"
    else:
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
