class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(-1)
        lptr = 0

        while lptr < len(nums):
            if nums[lptr] == -1 or nums[lptr] == lptr:
                lptr += 1
                continue
                
            nums[nums[lptr]], nums[lptr] = nums[lptr], nums[nums[lptr]]

        return nums.index(-1)