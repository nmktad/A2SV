class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        color = [0] * (n + 1)
        graph = defaultdict(list)

        for fr, to in dislikes:
            graph[fr].append(to)
            graph[to].append(fr)

        def dfs(node, c):
            
            color[node] = c

            for neighbor in graph[node]:
                if color[neighbor] == c:
                    return False
                else:
                    if not color[neighbor]:
                        res = dfs(neighbor, -c)

                        if not res:
                            return False

            return True
        
        for p in range(1, n+1):
            if not color[p]:
                if not dfs(p, 1):
                    return False

        return True