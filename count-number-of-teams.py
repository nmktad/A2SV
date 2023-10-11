class Solution:
    def numTeams(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = [0] * n, [0] * n

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    left[i] += 1

                if nums[i] < nums[j]:
                    right[j] += 1
        
        ans = 0
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    ans += left[j]
                
                if nums[i] < nums[j]:
                    ans += right[i]

        return ans