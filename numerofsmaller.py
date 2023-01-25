len1, len2 = map(int, input().split())
 
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
 
ans = []
 
tptr = 0
 
for val in list2:
    while tptr < len1 and val > list1[tptr]:
        tptr += 1
    
    ans.append(tptr)
    
print(*ans)
