class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [inf] * len(nums)
        dp[0] = 0

        for i in range(len(nums)):
            for j in range(1, nums[i]+1):
                if i+j >= len(nums): continue
                
                dp[i+j] = min(dp[i+j], dp[i]+1) 
        
        return dp[-1]