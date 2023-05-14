n, m, k = map(int, input().split())
 
emote = list(map(int, input().split()))
 
maxnum = max(emote)
emote.remove(maxnum)
maxnum2 = max(emote)
 
cycle = m // (k + 1)
rem = m % (k + 1)
 
print((((k * maxnum) + maxnum2) * cycle) + maxnum * rem)