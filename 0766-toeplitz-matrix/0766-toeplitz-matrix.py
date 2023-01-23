from collections import Counter

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        cbptr = len(matrix) - 1
        ctptr = 0
        
        while cbptr >= 0:
            diagonal = []
            x, y = cbptr, ctptr
            print(x, y)
            while x < len(matrix) and y < len(matrix[0]):
                diagonal.append(matrix[x][y])
                x += 1
                y += 1
            
            print(diagonal)
            if len(diagonal) != 1:
                count = Counter(diagonal)
                print(count)
                if count[matrix[cbptr][ctptr]] != len(diagonal):
                    return False
            
            cbptr -= 1
            
        cbptr = 0
        ctptr = len(matrix[0]) - 1
        
        while ctptr > 0:
            diagonal = []
            x, y = cbptr, ctptr
            
            while x < len(matrix) and y < len(matrix[0]):
                diagonal.append(matrix[x][y])
                x += 1
                y += 1
                
            print(diagonal)
            if len(diagonal) != 1:
                count = Counter(diagonal)
                print(count)
                if count[matrix[cbptr][ctptr]] != len(diagonal):
                    return False
            
            ctptr -= 1
            
        return True
            
        