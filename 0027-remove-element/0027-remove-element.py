class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        iptr = 0
        jptr = 0
        
        k = -1
        
        while iptr < len(nums):
            if nums[iptr] != val and nums[jptr] == val:
                nums[iptr], nums[jptr] = nums[jptr], nums[iptr]
            if nums[jptr] != val:
                jptr += 1
                k = jptr
            
            iptr += 1       
        
        if len(nums) != 0:  
            for i in range(len(nums)-1, k-1, -1):
                if i >= 0:                 
                    print(f"nums to be erased {nums[i]}", i)
                    nums[i] = "_"

        if k == -1 or len(nums) == 0:
            return 0
        else:
            return k