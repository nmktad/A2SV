import sys
import math
import bisect
import heapq
import itertools
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict, Counter, deque
from bisect import bisect_left,bisect_right, insort_left, insort_right
 
mod=1000000007
 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()
def get_int(): return int(sys.stdin.readline().strip())
def get_list_strings(): return list(map(str, sys.stdin.readline().strip().split()))
 
t = get_int()
 
for _ in range(t):
    n = get_int()
    mlist = get_list()
    
    power = 0
    i = 0
    
    while i < n:
        while mlist[i] % 2 == 0:
            mlist[i] //= 2
            power += 1
            
        i += 1
        
    maxval = max(mlist)
    
    print(((2 ** power) * maxval) + sum(mlist) - maxval)