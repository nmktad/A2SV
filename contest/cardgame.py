n = int(input())

mylist = list(map(int, input().split()))

left = 0
right = n -1

ans = [0, 0]

turn = False

while right >= left:
    if mylist[right] > mylist[left]:
        ans[turn] += mylist[right]
        right -= 1
    else:
        ans[turn] += mylist[left]
        left += 1
        
    turn = not turn
    
print(*ans)
