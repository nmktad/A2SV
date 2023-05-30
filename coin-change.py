class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount: return 0

        memo = {}

        def dp(tar):
            if tar == 0:
                return 0

            if tar not in memo:
                memo[tar] = inf

                for coin in coins:
                    if tar-coin >= 0:
                        memo[tar] = min(dp(tar-coin), memo[tar])
                
            return memo[tar] + 1

        ans =  dp(amount)

        if ans == inf:
            return -1
        else:
            return ans