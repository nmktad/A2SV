class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        isValid = lambda r, c: 0 <= r < len(grid1) and 0 <= c < len(grid1[0])

        def dfs(row, col):
            nonlocal subset        

            if grid1[row][col] == 0:
                subset = 0
                return

            grid2[row][col] = 0

            for rc, cc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr = row + rc
                nc = col + cc
                
                if isValid(nr, nc) and grid2[nr][nc]:
                    dfs(nr, nc)

        ans = 0

        for row in range(len(grid1)):
            for col in range(len(grid1[0])):
                if grid1[row][col] == grid2[row][col] == 1:
                    subset = 1
                    dfs(row, col)
                    ans += subset
        return ans