class Solution:
    def calculateMinimumHP(self, nums: List[List[int]]) -> int:
        m, n = len(nums), len(nums[0])

        dp = [[inf] * (n+1)  for _ in range(m+1)]

        dp[m-1][n] = 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = max(min(dp[i+1][j], dp[i][j+1])-nums[i][j], 1)
        
        return dp[0][0]