num =  int(input())
 
for _ in range(num):
    [rside1, rside2] = list(map(int, input().split()))
    [r2side1, r2side2] = list(map(int, input().split()))
    
    _max = max(rside1, rside2)
    
    if _max in [rside1, rside2] and _max in [r2side1, r2side2]:
        if _max == rside1 and _max - rside2 in [r2side1, r2side2]:
            print("YES")
        elif _max == rside2 and _max - rside1 in [r2side1, r2side2]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
