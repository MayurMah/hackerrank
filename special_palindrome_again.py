#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    n = len(s)

    pcount = 0
    plist = list()
    cur_count = 0
    prev_char = ''
    cur_char = ''
    listcount = 0
    for i in range(n):
        cur_char = s[i]
        if(i==0):
            cur_count=1
            plist.append({cur_char:cur_count})
        elif(cur_char==prev_char):
            cur_count += 1
            plist[listcount][cur_char]  = cur_count
        else:
            cur_count = 1
            listcount += 1
            plist.append({cur_char:cur_count})
        prev_char = cur_char

    #print(plist)

    for i,x in enumerate(plist):
        cur_val = list(x.values())[0]
        if(cur_val>1):
            pcount += int(cur_val*(cur_val+1)/2)
        if(cur_val==1):
            pcount += 1
            if(i!=0 and i!=len(plist)-1):
                if(list(plist[i-1].keys()) == list(plist[i+1].keys())):
                    pcount += min(list(plist[i-1].values())[0],list(plist[i+1].values())[0])

    #print(pcount)
    return pcount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
