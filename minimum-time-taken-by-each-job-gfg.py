class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        graph = defaultdict(list)
        indegree = [0] * (n + 1)
    
        for fr, to in edges:
            graph[fr].append(to)
            indegree[to] += 1
    
        queue = deque()
    
        for i in range(1, n+1):
            if indegree[i] == 0:
                queue.append(i)
        
        ans = [0] * (n + 1)
        
        time = 1
    
        while queue:
            l = len(queue)
    
            for _ in range(l):
                curr = queue.popleft()
                ans[curr] = time
    
                for nbr in graph[curr]:
                    indegree[nbr] -= 1

                    if indegree[nbr] == 0:
                        queue.append(nbr)
                        
            time += 1
    
        return ' '.join(map(str, ans[1:]))