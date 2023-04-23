class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1,0), (0, -1), (0,1)]

        visited = set()

        def findIslandArea(row, col):
            if grid[row][col] == 0:
                return 0

            visited.add((row, col))
            count = 0

            for direction in directions:
                newRow, newCol = row + direction[0], col + direction[1]
                
                if newRow >= 0 and newRow < len(grid) and newCol >= 0 and newCol < len(grid[0]):
                    if (newRow, newCol) not in visited:
                        count += findIslandArea(newRow, newCol)

            return count + 1

        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == 1:
                    visited.add((i, j))
                    ans = max(ans, findIslandArea(i, j))

        return ans