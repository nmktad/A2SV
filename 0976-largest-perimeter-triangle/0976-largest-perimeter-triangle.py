class Solution:
    
    
    def largestPerimeter(self, nums: List[int]) -> int:
        def check_triangle(nums):
            print("nums to be checked", nums)
            if nums[0] + nums[1] > nums[2] and nums[1] + nums[2] > nums[1] and nums[2] + nums[1] > nums[0]:
                return nums[0] + nums[1] + nums[2]
            else:
                return 0
        
        nums.sort()
        
        l_ptr = 0
        r_ptr = 3
        ans = 0
        
        while r_ptr <= len(nums):            
            ans = max(ans, check_triangle(nums[l_ptr:r_ptr]))
            
            l_ptr += 1
            r_ptr += 1
            
        return ans
                
            
            
            