class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        @cache
        def dp(i, j):
            if i >= len(satisfaction):
                return 0
        
            return max(j*satisfaction[i] + dp(i+1, j+1), dp(i+1, j))
        return dp(0, 1)