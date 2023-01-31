for _ in range(int(input())):
    n = int(input())
    myList = list(map(int, input().split()))
    
    lptr = 0
    rptr = lptr + 1
    
    myList.sort()
    
    while rptr < n:
        if myList[lptr] == myList[rptr]:
            myList[lptr] = None
        else:
            if abs(myList[lptr] - myList[rptr]) == 1:
                if myList[lptr] < myList[rptr]:
                    myList[lptr] = None
                else:
                    myList[rptr] = None
        
        lptr += 1
        rptr += 1
        
    if myList.count(None) + 1 == n:
        print("YES")
    else: 
        print("NO")
