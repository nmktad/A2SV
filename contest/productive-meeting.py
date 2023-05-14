import heapq
 
for _ in range(int(input())):
    n = int(input())
    
    arr = list(map(lambda x: int(x) * -1, input().split()))
    arr = [(arr[i], i+1) for i in range(len(arr))]
    
    heapq.heapify(arr)
    
    hist = []
    count = 0
    
    while len(arr) > 1:
        x, y = heapq.heappop(arr), heapq.heappop(arr)
        
        if x[0] < 0 and y[0] < 0:
            hist.append((x[1], y[1]))
            count += 1
            
        x, y = (x[0] + 1, x[1]), (y[0] + 1, y[1])
        
        if x[0] < 0:
            heapq.heappush(arr, x)
        
        if y[0] < 0:
            heapq.heappush(arr, y)
    
    print(count)
    for x, y in hist:
        print(x, y)
