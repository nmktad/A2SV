for _ in range(int(input())):
    grid = []
    
    n = int(input())
    
    for _ in range(2):
        temp = []
        
        for char in input():
            temp.append(char)
            
        grid.append(temp)
    
    directions = [(-1,0),(1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,1),(1,-1)]
    isValid = lambda r, c: 0 <= r < 2 and 0 <= c < n
    visited = set()
    
    def dfs(row, col):
        if (row, col) == (1, n - 1):
            return True
        
        flag = False
        
        for r, c in directions:
            nrow, ncol = row + r, col + c
            
            if isValid(nrow, ncol) and (nrow, ncol) not in visited and  grid[nrow][ncol] == '0':
                visited.add((nrow, ncol))
                if dfs(nrow, ncol):
                    flag = True
                    
        return flag
        
    if dfs(0,0):
        print("YES")
    else:
        print("NO")