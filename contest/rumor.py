from collections import defaultdict, deque
 
n, m = map(int, input().split())
 
graph = defaultdict(list)
 
bribes = list(map(int, input().split()))
 
for _ in range(m):
    fr, to = map(int, input().split())
    graph[fr].append(to)
    graph[to].append(fr)
    
visited = set()
 
coins = 0
            
queue = deque()
 
for key in range(1, n+1):
    if key not in visited:
        queue.append(key)
        visited.add(key)
        pathbribe = float('inf')
        
        while queue:
            l = len(queue)
            
            for _ in range(l):
                curr = queue.popleft()
                
                
                pathbribe = min(pathbribe, bribes[curr-1])
                
                for nbr in graph[curr]:
                    if nbr not in visited:
                        queue.append(nbr)
                        visited.add(nbr)
                        
        coins += pathbribe
        
print(coins)