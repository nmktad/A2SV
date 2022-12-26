class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l_ptr = 0
        r_ptr = len(nums) - 1
        
        while l_ptr < r_ptr:
            if nums[l_ptr] % 2 != 0:
                nums[l_ptr], nums[r_ptr] = nums[r_ptr], nums[l_ptr]
                
                r_ptr -= 1
            else:
                l_ptr += 1
                
        return nums
            
            