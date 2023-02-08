class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    rows.add(row)
                    cols.add(col)
        
        for row in range(len(matrix)):
            if row in rows:
                for col in range(len(matrix[0])):
                    matrix[row][col] = 0
                    
        for col in range(len(matrix[0])):
            if col in cols:
                for row in range(len(matrix)):
                    matrix[row][col] = 0