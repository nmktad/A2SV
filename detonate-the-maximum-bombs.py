class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i, (xi, yi, ri) in enumerate(bombs):
            for j, (xj, yj, rj) in enumerate(bombs):
                if i != j and (xi-xj)**2 + (yi-yj)**2 <= ri**2:
                    graph[i].append(j)

        visited = set()

        def dfs(node):
            visited.add(node)
            
            con = 0

            for neighbor in graph[node]:
                if neighbor not in visited:
                    con += dfs(neighbor)
            
            return con + 1

        ans = 0
        
        for vertex in range(len(bombs)):
            ans = max(ans, dfs(vertex))
            visited.clear()
        
        return ans