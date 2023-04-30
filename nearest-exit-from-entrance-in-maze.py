class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])

        queue = deque([tuple(entrance)])
        visited = set([tuple(entrance)])

        checkIfItsExit = lambda r, c: r == 0 or r == m - 1 or c == 0 or c == n - 1
        isValid = lambda r, c: 0 <= r < m and 0 <= c < n

        step = 0

        directions = [(0,1), (0, -1), (1,0), (-1,0)]

        while queue:
            l = len(queue)

            for _ in range(l):
                crow, ccol = queue.popleft()

                if (crow, ccol) != tuple(entrance):
                    flag = checkIfItsExit(crow, ccol)

                    if flag:
                        return step

                for r, c in directions:
                    nrow, ncol = crow+r, ccol+c

                    if isValid(nrow, ncol) and (nrow, ncol) not in visited and maze[nrow][ncol] == '.':
                        queue.append((nrow, ncol))
                        visited.add((nrow, ncol))

            step += 1
            

        return -1