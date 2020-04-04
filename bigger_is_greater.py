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

    # Return 'no answer' if the word has only one unique character
    if len(set(w)) == 1:
        return result

    # Find position & char to replace
    to_replace_pos = -1
    to_replace_char = ''
    max_char_seen = w[len(w) - 1]

    for i in range(len(w) - 2, -1, -1):
        if ord(max_char_seen) > ord(w[i]):
            to_replace_pos = i
            to_replace_char = w[i]
            break
        else:
            max_char_seen = w[i]

    # Return 'no answer' if no character is to be replaced
    if to_replace_pos == -1:
        return result

    # Find position and char to replace with
    replace_with_char = '{'  # character with ASCII value greater than that of 'Z'
    replace_with_pos = -1

    for j in range(to_replace_pos + 1, len(w)):
        if ord(to_replace_char) < ord(w[j]) < ord(replace_with_char):
            replace_with_char = w[j]
            replace_with_pos = j

    # Return 'no answer' if no character found to replace with
    if replace_with_pos == -1:
        return result

    # Swap the to_replace and replace_with characters and sort the rest of the string
    temp = (w[to_replace_pos + 1:replace_with_pos] + to_replace_char + w[replace_with_pos + 1:])
    result = w[0:to_replace_pos] + replace_with_char + ''.join(sorted(temp))

    # Return the result is the result is different from the original string. Otherwise, return 'no answer'
    return result if result != original else "no answer"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
