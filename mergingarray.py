len1, len2 = map(int, input().split())
 
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
 
ptr1 = 0
ptr2 = 0
 
ans = []
 
while ptr1 < len1 and ptr2 < len2:
    if list1[ptr1] < list2[ptr2]:
        ans.append(list1[ptr1])
        ptr1 += 1
    else:
        ans.append(list2[ptr2])
        ptr2 += 1
 
if ptr1 < len1:
    ans.extend(list1[ptr1:])
if ptr2 < len2:
    ans.extend(list2[ptr2:])
    
print(*ans)
