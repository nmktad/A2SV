class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        empty = []
        excess = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    empty.append((i,j))
                elif grid[i][j] > 1:
                    excess.append((i,j))

        if not empty: return 0

        res = inf

        for si,sj in empty:
            for ti,tj in excess:
                grid[si][sj] = 1
                grid[ti][tj] -= 1

                res = min(res, abs(si-ti) + abs(sj-tj) + self.minimumMoves(grid))

                grid[si][sj] = 0
                grid[ti][tj] += 1

        return res