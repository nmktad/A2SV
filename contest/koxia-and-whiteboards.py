import heapq

for _ in range(int(input())):
    n, m = map(int, input().split())
    
    arr = list(map(int, input().split()))
    cha = list(map(int, input().split()))
    
    heapq.heapify(arr)
    
    for val in cha:
        heapq.heappop(arr)
        heapq.heappush(arr, val)
        
    print(sum(arr))
    
    
    
    