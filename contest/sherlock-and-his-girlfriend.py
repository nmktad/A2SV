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
 
n = get_int()
 
ans = [1 for _ in range(n+2)]
ans[1], ans[0] = 0,0
 
i = 2
 
while i * i <= n+1:
    if ans[i] == 1:
        j = i * i
        
        while j <= n + 1:
            ans[j] = 2
            j += i
        
    i += 1
 
if n < 3:
    print(1)
else:
    print(2)
print(*ans[2:])