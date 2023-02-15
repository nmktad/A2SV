class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        lptr = 0
        rptr = len(nums) - 1
        
        count = 0
        
        while rptr > lptr:
            if nums[rptr] + nums[lptr] == k:
                count += 1
                rptr -= 1
                lptr += 1
            elif nums[rptr] + nums[lptr] > k:
                rptr -= 1
            else:
                lptr += 1
                
        return count