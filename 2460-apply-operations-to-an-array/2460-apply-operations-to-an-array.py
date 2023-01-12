class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        lptr = 0
        rptr = lptr + 1
        
        while rptr < len(nums):
            if nums[lptr] == nums[rptr]:
                nums[lptr] *= 2
                nums[rptr] = 0
            lptr += 1
            rptr += 1
        
        lptr = 0
        rptr = 0
        
        while rptr < len(nums):
            if nums[rptr] != 0:
                nums[lptr], nums[rptr] = nums[rptr], nums[lptr]
                lptr += 1
            
            rptr += 1
        return(nums)