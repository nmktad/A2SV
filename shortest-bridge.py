class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        '''
        [
         [1,1,1,1,1],
         [1,0,0,0,1],
         [1,0,1,0,1],
         [1,0,0,0,1],
         [1,1,1,1,1]
        ]
        '''
        n = len(grid)

        isValid = lambda r, c: 0 <= r < n and 0 <= c < n

        queue = deque()
        island = set()

        def dfs(crow, ccol):
           
            island.add((crow, ccol))
            queue.append((crow, ccol))

            for r, c in [(0,1), (0, -1), (1,0), (-1,0)]:
                nrow, ncol = crow + r, ccol + c

                if isValid(nrow, ncol) and (nrow, ncol) not in island and grid[nrow][ncol] == 1:
                    dfs(nrow, ncol)

        flag = True

        for row in range(n):
            if flag:
                for col in range(n):
                    if grid[row][col] == 1:
                        dfs(row, col)

                        # print('the island is', island)
                        
                        length = 0
                        visited = set()

                        while queue:
                            # print(queue)

                            l = len(queue)

                            for _ in range(l):
                                crow, ccol = queue.popleft()

                                for r, c in [(0,1), (0, -1), (1,0), (-1,0)]:
                                    nrow, ncol = crow + r, ccol + c

                                    
                                    if isValid(nrow, ncol):
                                        if ((nrow, ncol) not in island and 
                                            grid[nrow][ncol] == 1):
                                            return length

                                        if ((nrow, ncol) not in island and 
                                            (nrow, ncol) not in visited and 
                                            grid[nrow][ncol] == 0):

                                            visited.add((nrow, ncol))
                                            queue.append((nrow, ncol))

                            length += 1