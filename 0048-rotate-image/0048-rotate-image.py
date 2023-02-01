class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # reverse the matrix from bottom to top
        top = 0
        bottom = len(matrix) - 1
        
        while bottom > top:
            matrix[top], matrix[bottom] = matrix[bottom], matrix[top]
            
            bottom -= 1
            top += 1
        
        for i in range(len(matrix)):
            x, y = 0, i
            transposeX, transposeY = y, x
            
            while x < transposeX and y > transposeY:
                transposeX, transposeY = y, x
                matrix[x][y], matrix[transposeX][transposeY] = matrix[transposeX][transposeY], matrix[x][y]
                
                x += 1
                y -= 1
            
        for i in range(len(matrix) - 1, 0, -1):
            x, y = i, len(matrix) - 1
            transposeX, transposeY = y, x
            
            
            while x < transposeX and y > transposeY:
                transposeX, transposeY = y, x

                matrix[x][y], matrix[transposeX][transposeY] = matrix[transposeX][transposeY], matrix[x][y]
                
                x += 1
                y -= 1
            
                