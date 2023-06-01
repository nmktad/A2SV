class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = {}

        def dp(n):       
            if n < 2:
                return n

            if n not in memo:
                if n % 2 == 0:
                    memo[n] = dp(n//2)
                else:
                    memo[n] = dp(n//2) + dp((n//2) + 1)

            return memo[n]

        return max(dp(i) for i in range(n+1))