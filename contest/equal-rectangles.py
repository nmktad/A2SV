for _ in range(int(input())):
    norect = int(input())
    
    sticks = list(map(int, input().split()))
    
    sticks.sort()
    
    area = sticks[0] * sticks[-1]
    
    ans = "YES"
    
    for i in range(norect):
        l = 2 * i
        r = (4 * norect) - (2 * i) - 2
        
        if sticks[l] != sticks [l + 1] or sticks[r] != sticks[r + 1] or sticks[l] * sticks[r] != area:
            ans = "NO"
            break
    
    print(ans)