class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        parent = {}
        for i in range(1,row+1):
            for j in range(1,col+1):
                parent[(i,j)] = (i,j)

        matrix = [[0]*col for i in range(row)]
        
        isValid = lambda x, y: 0 <= x < row and 0 <= y < col and matrix[x][y] == 1
        
        def find(child):
            if child != parent[child]: 
                parent[child] = find(parent[child])
                
            return parent[child]
        
        def union(cell1, cell2): 
            x = find(cell1)
            y = find(cell2)

            if (x[0] == 1 and y[0] == row) or (x[0] == row and y[0] == 1): 
                return True

            if x[0] == 1 or x[0] == row:
                parent[y] = x
            else:
                parent[x] = y

            return False
        
        for i in range(len(cells)-1, -1, -1):
            r, c = cells[i][0]-1, cells[i][1]-1

            matrix[r][c] = 1

            for j,k in directions:
                x,y = r + j, c + k
                z = False
                if isValid(x,y):
                    z = union((x+1,y+1),(r+1,c+1))
                if z: 
                    return i