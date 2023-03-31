for _ in range(int(input())):
    x = int(input())
    y = 1
    
    if x == 1:
        print(3)
        continue
    
    while x & y == 0:
        y = y << 1
     
    onecount = 0
    temp = x
    
    while temp != 0:
        onecount += temp & 1
        temp = temp >> 1
    
    if onecount > 1:
        print(y)
    else:
        y |= 1
        print(y)
        