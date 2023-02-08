class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        currRow = 0
        currCol = 0
        minRow = 0
        minCol = 0
        col = len(matrix[0])
        row = len(matrix)
        total = len(matrix) * len(matrix[0])
        
        while len(ans) != total:
            while currCol < col:
                ans.append(matrix[currRow][currCol])
                currCol += 1
            
            currCol -= 1
            currRow += 1
            minRow += 1
            
            if len(ans) == total:
                break
            
            while currRow < row:
                ans.append(matrix[currRow][currCol])
                currRow += 1
                    
            currRow -= 1
            currCol -= 1
            col -= 1
            
            if len(ans) == total:
                break
            
            while currCol >= minCol:
                ans.append(matrix[currRow][currCol])
                currCol -= 1
                    
            currCol += 1
            currRow -= 1 
            row -= 1
            
            if len(ans) == total:
                break
            
            while currRow >= minRow:
                ans.append(matrix[currRow][currCol])
                currRow -= 1
                    
            currRow += 1
            currCol += 1
            minCol += 1
            
            if len(ans) == total:
                break
            
        return ans