class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = []
        
        for iptr, val in enumerate(nums):
            jptr = iptr+1
            
            while jptr < len(nums) and iptr < jptr:
                if nums[iptr] == nums[jptr]:
                    ans.append([iptr, jptr])
                    
                jptr += 1
        print(ans)
        
        return len(ans)