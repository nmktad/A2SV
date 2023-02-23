class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        presum = [0]
        
        for val in nums:
            presum.append(val + presum[-1])
        
        del presum[0]
        
        return presum