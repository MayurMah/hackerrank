#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):

    original = w
    result = "no answer"

    if len(set(w)) == 1:
        return result 
    
    # Find position & char to replace 
    to_replace_pos =  -1
    to_replace_char = ''
    max_char_seen = w[len(w)-1]
    
    for i in range(len(w)-2,-1,-1):
        if ord(max_char_seen) > ord(w[i]):
            to_replace_pos = i
            to_replace_char = w[i]
            break
        else:
            max_char_seen = w[i]

    if to_replace_pos == -1:
        return result

    # print("cp1",to_replace_pos)

    # Find position and char to replace with
    replace_with_char = '{'
    replace_with_pos = -1

    for j in range(to_replace_pos+1,len(w)):
        if ord(w[j])>ord(to_replace_char) and ord(w[j]) < ord(replace_with_char):
            replace_with_char = w[j]
            replace_with_pos = j 

    if replace_with_pos == -1:
        return result
    
    # print("cp2",replace_with_pos)
                
    temp = (w[to_replace_pos+1:replace_with_pos] + to_replace_char + w[replace_with_pos+1:])

    result = w[0:to_replace_pos] + replace_with_char + ''.join(sorted(temp))

    # print("cp3",result,original)

    return result if result != original else "no answer"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
