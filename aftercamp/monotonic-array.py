class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isIncreasing = isDecreasing = True

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]: isIncreasing = False

            if nums[i] < nums[i+1]: isDecreasing  = False

        return isIncreasing or isDecreasing

        

        