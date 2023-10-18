class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = ceil(total/2)

        @cache
        def dp(i, t):
            if t >= target or i == len(stones):
                return abs(t - (total - t))

            return min(dp(i+1, t + stones[i]), dp(i+1, t))

        return dp(0, 0)