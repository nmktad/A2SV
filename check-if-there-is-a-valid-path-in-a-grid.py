class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        rep = {(i, j):(i, j) for i, j in product(range(m), range(n))}

        edges = {1: ('L', 'R'), 2: ('U', 'D'), 3:('L', 'D'), 
                4:('D', 'R'), 5: ('U', 'L'), 6:('U', 'R')}

        steps = {'L': (0, -1), 'R': (0, 1), 'D':(1, 0), 'U':(-1, 0)}

        opp = {'L': 'R', 'R': 'L', 'D': 'U', 'U': 'D'}

        isValid = lambda x, y: 0 <= x < m and 0 <= y < n
        
        def find(x):
            if rep[x] == x:
                return x
            
            rep[x] = find(rep[x])
            return rep[x]

        rank = defaultdict(lambda:1)
        
        def union(col1, col2):
            rep1, rep2 = find(col1), find(col2)

            if rep1 != rep2:
                if rank[rep1] > rank[rep2]:
                    rep[rep2] = rep1
                    rank[rep1] += rank[rep2]
                else:
                    rep[rep1] = rep2
                    rank[rep2] += rank[rep1]
  
        for r in range(m):
            for c in range(n):
                tile = grid[r][c]
                for dir in edges[tile]:
                    nr, nc = r + steps[dir][0], c + steps[dir][1]

                    if isValid(nr, nc):
                        if opp[dir] in edges[grid[nr][nc]]:
                            union((r, c), (nr, nc))

        return find((0, 0)) == find((m-1, n-1))