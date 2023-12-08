class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        prevdp = [[0] * n for _ in range(n)]
        currdp = [[0] * n for _ in range(n)]

        prevdp[row][column] = 1

        for _ in range(k):
            for i in range(n):
                for j in range(n):
                    currdp[i][j] = 0

                    for nx, ny in [
                        (i-1, j-2), (i-1, j+2), 
                        (i+1, j-2), (i+1, j+2), 
                        (i-2, j+1), (i+2, j-1), 
                        (i-2, j-1), (i+2, j+1)]:

                        if 0 <= nx < n and 0 <= ny < n:
                            currdp[i][j] += prevdp[nx][ny] / 8

            prevdp, currdp = currdp, prevdp
        
        return sum(prevdp[i][j] for i in range(n) for j in range(n))