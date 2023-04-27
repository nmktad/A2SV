class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(-1,0),(1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,1),(1,-1)]

        if grid[0][0] == 1:
            return -1

        queue = deque([(0,0)])

        m,n = len(grid), len(grid[0])

        isValid = lambda r, c: 0 <= r < m and 0 <= c < n

        count = 1

        while queue:
            count += 1
            cl = len(queue)

            for _ in range(cl):
                curr = queue.popleft()

                if grid[curr[0]][curr[1]] != 1:
                    grid[curr[0]][curr[1]] = 1

                if curr == (m-1, n-1):
                    print(grid)
                    return count - 1

                print(curr)

                for r, c in directions:
                    new_row, new_col = curr[0] + r, curr[1] + c

                    if isValid(new_row, new_col) and grid[new_row][new_col] == 0:
                        queue.append((new_row, new_col))
                        grid[new_row][new_col] = 1

        return -1