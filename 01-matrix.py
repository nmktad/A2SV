class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        visited = set()

        m, n = len(mat), len(mat[0])

        directions = [(0, -1), (0, 1), (-1, 0), (1,0)]
        isValid = lambda r, c: 0 <= r < m and 0 <= c < n

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    queue.append((row, col))
                    visited.add((row, col))

        length = 0

        while queue:
            cl = len(queue)

            for _ in range(cl):
                crow, ccol = queue.popleft()

                mat[crow][ccol] = length

                for r, c in directions:
                    newr, newc = crow + r, ccol + c

                    if isValid(newr, newc) and (newr, newc) not in visited:
                        queue.append((newr, newc))
                        visited.add((newr, newc))
            

            length += 1

        return mat