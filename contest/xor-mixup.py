for _ in range(int(input())):
    n = int(input())
    
    mlist = list(map(int, input().split()))
    
    for i,val in enumerate(mlist):
        temp, idx = 0, 0 
        
        # print('checking for', val)
        
        for j in range(n):
            if j != i:
                idx = j + 1
                temp = mlist[j]
                break
        
        while idx < n:
            if i == idx:
                # print('the num it self', mlist[idx])
                idx += 1
                continue
            
            # print('about to xor', temp, 'and', mlist[idx])
        
            temp ^= mlist[idx]
            idx += 1
            
        # print('what is temp', temp)
      
        if temp == val:
            print(val)
            break