class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.presum = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        
        for row in range(1, len(matrix) + 1):
            for col in range(1, len(matrix[0]) + 1):
                self.presum[row][col] = self.presum[row - 1][col] + self.presum[row][col-1] + matrix[row-1][col-1] - self.presum[row-1][col-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
      
        minrow = min(row1, row2)
        maxrow = max(row1, row2)
        mincol = min(col1, col2)
        maxcol = max(col1, col2)
        
        return self.presum[maxrow+1][maxcol+1] + self.presum[minrow][mincol] - self.presum[minrow][maxcol+1] - self.presum[maxrow+1][mincol]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)