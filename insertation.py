#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    for i in range (n):
        for j in range (n-1):
            x=arr[j]
            y=arr[j+1]
            if x>y:
                arr[j+1]=x
                print(' '.join(map(str, arr)))
                arr[j]=y
    print(' '.join(map(str, arr)))
            
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
