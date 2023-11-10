class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        n = len(mat)-1

        for i in range(n+1):
            ans += mat[i][i] + mat[i][n-i]
            if i == n-i:
                ans -= mat[i][i]
        return ans
