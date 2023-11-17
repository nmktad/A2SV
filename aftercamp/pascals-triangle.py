class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[0] * i for i in range(1, numRows + 1)]
        dp[0][0] = 1

        for i in range(numRows-1):
            for j in range(len(dp[i])):
                dp[i+1][j] += dp[i][j]
                dp[i+1][j+1] += dp[i][j]

        return dp





        