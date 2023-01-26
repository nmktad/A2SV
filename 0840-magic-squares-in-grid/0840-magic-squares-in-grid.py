class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        counter = 0
        
        
        for i in range(len(grid)-2):  
            for j in range(len(grid[0])-2):
                flag = True
                visited = set()
                
                for xitr in range(i, i+3):
                    for yitr in range(j, j+3):
                        if grid[xitr][yitr] < 10 and grid[xitr][yitr] > 0:
                            visited.add(grid[xitr][yitr])
                        
                if len(visited) != 9:
                    continue
                
                        
                
                # calculate the first row sum and compare it to all the others
                if flag ==True:
                    target = 0   

                    for itr in range(j, j+3):
                        target += grid[i][itr]
                    
                        print("target", target, grid[0][itr])
                    for iitr in range(i+1, i+3):
                        _sum = 0
                        for jitr in range(j, j+3):
                            _sum += grid[iitr][jitr]
                            print(_sum, grid[iitr][jitr])
                        if _sum !=target:
                            flag = False
                            break
                            
                    if flag == False:
                        print("about to break")
                        continue
                        
                    for jitr in range(j, j+3):
                        _sum = 0
                        for iitr in range(i, i+3):                        
                            _sum += grid[iitr][jitr]
                            print(_sum, grid[iitr][jitr])
                        if _sum !=target:
                            flag = False
                            break
                            
                    if flag == False:
                        print("about to break")
                        continue
                        
                    iitr = i
                    jitr = j
                    diagonalSum = 0
                    
                    print("before diagonals", iitr, jitr)
                    
                    while iitr < i+3 and jitr < j+3:
                        diagonalSum += grid[iitr][jitr]
                        print("diagonal sum", grid[iitr][jitr], diagonalSum) 
                        iitr += 1
                        jitr += 1
                        
                    if diagonalSum != target:
                        print("about to end")
                        continue
                        
                    diagonalSum = 0
                    iitr = i
                    jitr = j + 2
                    
                    while iitr < i + 3 and jitr >=  j:
                        diagonalSum += grid[iitr][jitr]
                        print("diagonal sum", grid[iitr][jitr], diagonalSum) 
                        iitr += 1
                        jitr -= 1
                        
                    if diagonalSum != target:
                        print("about to end")
                        continue
                        
                    counter += 1
                    print("counter now is", counter )
        
        return counter