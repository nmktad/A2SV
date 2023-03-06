class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # return bisect_left(nums, target)

        l = 0
        r = len(nums) - 1
        a = len(nums)

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] >= target:
                a = m
                r = m - 1
            else:
                l = m + 1

        return a