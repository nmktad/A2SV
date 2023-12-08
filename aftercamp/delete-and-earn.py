class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums = sorted([(num, freq) for num, freq in Counter(nums).items()])
        dp = [0] * len(nums)
        ans = 0

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i][0] + 1 == nums[j][0]:
                    continue
                
                dp[i] = max(dp[i], dp[j])

            dp[i] += nums[i][0] * nums[i][1]
            ans = max(ans, dp[i])

        return ans


            

        


        