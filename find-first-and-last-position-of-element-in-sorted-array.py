class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        a = b = len(nums)

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] >= target:
                if nums[m] == target:
                    a = m
                r = m - 1
            else:
                l = m + 1

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] <= target:
                if nums[m] == target:
                    b = m
                l = m + 1
            else:
                r = m - 1
        if a == len(nums) or b == len(nums): a = -1; b = -1
        return [a, b]