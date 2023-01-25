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
    temp = arr[n-1]
    
    for i in range(n-2, -2, -1):
        if i > -1 and arr[i] > temp:
            arr[i+1] = arr[i]
            print(*arr)
        else:
            arr[i + 1] = temp 
            print(*arr)
            break
        
        
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
