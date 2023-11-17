class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        
        heap = [(0, (0, 0))]
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        isValid = lambda x, y: 0 <= x < n and 0 <= y < m

        while heap:
            path, (x, y) = heapq.heappop(heap)

            if (x, y) in visited:
                continue

            visited.add((x, y))

            if x == n-1 and y == m - 1:
                return path

            for i, j in directions:
                nrow, ncol = x + i, y + j

                if isValid(nrow, ncol):
                    newpath = max(path, abs(heights[x][y] - heights[nrow][ncol]))
                    heapq.heappush(heap, (newpath, (nrow, ncol)))