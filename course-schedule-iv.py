class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        grid = [[False] * n for _ in range(n)]

        for pre, fr in prerequisites:
            grid[pre][fr] = True

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    grid[i][j] = grid[i][j] or grid[i][k] and grid[k][j]

        ans = []
        for fr, to in queries:
            ans.append(grid[fr][to])

        return ans