class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        queue = deque()
        seen = set()

        m, n = len(grid), len(grid[0])

        isKey = lambda r, c: (grid[r][c]).isalpha() and (grid[r][c]).islower()
        isLock = lambda r, c: (grid[r][c]).isalpha() and not (grid[r][c]).islower()
        nkeys = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    queue.append((i,j,0))
                    seen.add((i,j,0))
                
                if isKey(i, j):
                    nkeys += 1

        directions = [(-1, 0), (1, 0), (0, 1), (0,-1)]

        isValid = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[0])

        dist = 0

        keys = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}

        while queue:
            l = len(queue)

            for _ in range(l):
                cr, cc, state = queue.popleft()

                if state.bit_count() == nkeys:
                    return dist

                for r, c in directions:
                    nr, nc = cr + r, cc + c

                    if isValid(nr, nc) and grid[nr][nc] != "#":
                        if isKey(nr, nc):
                            nstate = state | (1 << keys[grid[nr][nc]])
                        else:
                            nstate = state

                        if isLock(nr, nc):
                            keyNeeded = grid[nr][nc].lower()

                            if not state & (1 << keys[keyNeeded]):
                                continue
                        
                        if (nr, nc, nstate) not in seen:
                            queue.append((nr, nc, nstate))
                            seen.add((nr, nc, nstate))
            
            dist += 1

        return -1