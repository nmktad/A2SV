from collections import defaultdict
 
graph = defaultdict(list)
 
for _ in range(int(input())):
    to, _, fr = input().split()
    
    graph[fr.lower()].append(to.lower())
 
def dfs(node):
   
    if not graph[node]:
        return 1
    
    maxDepth = 0
    
    for neighbor in graph[node]:
        maxDepth = max(maxDepth, dfs(neighbor))
 
    return maxDepth + 1
    
print(dfs("polycarp"))