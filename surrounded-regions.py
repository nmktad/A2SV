class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        direction= [(1,0), (-1,0), (0,1), (0,-1)]

        def isBorder(pos):
            return pos[0] == 0 or pos[0] == len(board)-1 or pos[1] == 0 or pos[1] == len(board[0])-1

        def dfs(pos):
            a , b = pos[0], pos[1]
            board[a][b]='Y'

            for x,y in direction:
                r, c = a + x, b + y

                if 0<=r<len(board) and 0<=c<len(board[0]) and board[r][c]=='O':
                    board[r][c]="Y"
                    dfs((r,c))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if isBorder((i,j)):
                    if board[i][j]=='O':
                        dfs((i,j))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='Y':
                    board[i][j]='O'