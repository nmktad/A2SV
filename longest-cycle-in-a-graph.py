class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        ans = -1
        color = [0] * len(edges)
        distance = defaultdict(int)

        def dfs(node, dist):
            nonlocal ans
            
            if color[node] == 2:
                return True

            if color[node] == 1:
                ans = max(ans, dist - distance[node])
                return False

            distance[node] = dist
            color[node] = 1
            
            if edges[node] != -1:
                dfs(edges[node], dist+1)
            
            color[node] = 2
        
        for i in range(len(edges)):
            if color[i] == 0:
                dfs(i,0)

        return ans