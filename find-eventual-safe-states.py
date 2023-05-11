class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = [0] * len(graph)
        ans = []

        def dfs(node):
            if color[node] == 2:
                return True

            elif color[node] == 0:
                color[node] = 1

                if all([dfs(nbr) for nbr in graph[node]]):
                    ans.append(node)
                    color[node] = 2
                    return True

            return False

        for i in range(len(graph)):
            dfs(i)

        return sorted(ans)