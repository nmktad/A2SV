class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2:
            return False

        tar = total // 2
        dp = [False] * (tar + 1) 
        dp[0] = True
        
        for num in nums:
            for i in range(tar, num-1, -1):
                dp[i] |= dp[i-num]

        return dp[tar]

        