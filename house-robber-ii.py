class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return max(nums)
        memo = {}

        def dp(i, end=0):
            if i < end:
                return 0

            if i not in memo:
                memo[i] = max(nums[i] + dp(i - 2, end), dp(i-1, end))

            return memo[i]

        curr = dp(len(nums)-2)
        memo.clear()
        return max(curr, dp(len(nums)-1, 1))