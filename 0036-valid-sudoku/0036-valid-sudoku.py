class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        checker = defaultdict(set)
        
        for row in range(9):
            for col in range(9):
                
                if board[row][col]==".":
                    continue

                box = (row//3, col//3)
                
                if board[row][col] in checker[row] or board[row][col] in checker[col+9] or board[row][col] in checker[box]:
                    return False
                else:
                    checker[row].add(board[row][col])
                    checker[col+9].add(board[row][col])
                    checker[box].add(board[row][col])
                
        return True
                
            