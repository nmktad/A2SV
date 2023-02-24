for _ in range(int(input())):
    n, m, k = map(int, input().split())
    
    ans = []
    
    finput = input()
    fstr = []
    
    sinput= input()
    sstr = []
    
    for char in finput:
        fstr.append(char)
        
    for char in sinput:
        sstr.append(char)
    
    fstr.sort()
    sstr.sort()
    
    fptr = 0
    sptr = 0
    
    turn = True
    
    if fstr[fptr] > sstr[sptr]:
        turn = False
    
    while fptr < n and sptr < m:
        for i in range(k):
            if fptr <n or sptr <m:
                # print(ans, fptr, "<", n, sptr, "<" , m)
                if turn:
                    if i == 0:
                        ans.append(fstr[fptr])
                        fptr += 1
                    else:
                        if fptr < n:
                            if fstr[fptr] <= sstr[sptr]:
                                ans.append(fstr[fptr])
                                fptr += 1
                            else:
                                break
                        else:
                            break
                else:
                    if i == 0:
                        ans.append(sstr[sptr])
                        sptr += 1
                    else:
                        if sptr < m:
                            if sstr[sptr] <= fstr[fptr]:
                                ans.append(sstr[sptr])
                                sptr += 1
                            else:
                                break
                        else:
                            break
            else: break
                
        turn = not turn
            
    print("".join(ans))
