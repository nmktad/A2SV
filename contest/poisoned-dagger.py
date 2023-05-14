def findTotal(arr, k):
    total = 0
    for i in range(len(arr) - 1):
        total += min(k, arr[i+1] - arr[i])
        
    return total + k
 
for _ in range(int(input())):
    n, h = map(int, input().split())
    
    mylist = list(map(int, input().split()))
    
    l = 1
    r = h
    
    ans = float('inf')
    
    while l <= r:
        m = l + (r - l) // 2
        
        totalTemp = findTotal(mylist, m)
        
        if  totalTemp >= h:
            r = m - 1
            ans = min(m, ans)
        else:
            l = m + 1
            
    print(ans)