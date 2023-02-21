for _ in range(int(input())):
    n = int(input())
    
    myList = list(map(int, input().split()))
    
    lptr = 0
    rptr = n - 1
    
    ans = []
    
    while lptr <= rptr:
        ans.append(myList[lptr])
        if lptr != rptr:
            ans.append(myList[rptr])
        lptr += 1
        rptr -= 1
    print(*ans)
