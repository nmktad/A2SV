class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        prevdp = [[0] * n for _ in range(n)]
        currdp = [[0] * n for _ in range(n)]

        prevdp[row][column] = 1

        for _ in range(k):
            for i in range(n):
                for j in range(n):
                    currdp[i][j] = 0

                    for x, y in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
                        newx, newy = i-x, j-y

                        if 0 <= newx < n and 0 <= newy < n:
                            currdp[i][j] += prevdp[newx][newy] / 8

            prevdp, currdp = currdp, prevdp
        
        return sum(prevdp[i][j] for i in range(n) for j in range(n))