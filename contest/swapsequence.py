n = int(input())
k = 0
myList = list(map(int, input().split()))
swaps = []
 
for i, val in enumerate(myList):
    _min = i
    
    for j in range(i+1, n):
        if myList[_min] > myList[j]:
            _min = j
    
    if _min != i:
        myList[i], myList[_min] = myList[_min], myList[i]
        swaps.append([i, _min])
        k += 1
        
print(k)
for val in swaps:
    print(*val)
