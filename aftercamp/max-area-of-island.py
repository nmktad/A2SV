class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        ans = 0
        isValid = lambda x, y: 0 <= x < len(grid) and 0 <= y < len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in seen and grid[i][j]:
                    q = deque([(i,j)])
                    seen.add((i, j))
                    rsum = 0

                    while q:
                        rsum += len(q)

                        for _ in range(len(q)):
                            x, y = q.popleft()

                            for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                                if isValid(nx, ny) and (nx, ny) not in seen and grid[nx][ny]:
                                    q.append((nx, ny))
                                    seen.add((nx,ny))
                    
                    ans = max(ans, rsum)
        return ans
                        
        