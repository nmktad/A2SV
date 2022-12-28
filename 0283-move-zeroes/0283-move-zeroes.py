class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) == 1:
            return nums
    
        iptr = 0
        jptr = 0
        
        while iptr < len(nums):
            if nums[iptr] != 0 and nums[jptr] == 0:
                nums[iptr], nums[jptr] = nums[jptr], nums[iptr]
            if nums[jptr] != 0:
                jptr += 1
            
            iptr += 1