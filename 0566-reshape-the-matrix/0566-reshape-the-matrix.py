class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        
        ans = [[0 for i in range(c)] for i in range(r)]
        
        for i in range(r * c):
            crow, ccol = i // len(mat[0]), i % len(mat[0])
            arow, acol = i // c, i % c
            
            ans[arow][acol] = mat[crow][ccol]            

        return ans
    