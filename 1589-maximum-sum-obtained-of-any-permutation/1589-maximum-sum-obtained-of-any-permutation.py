class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        if len(nums) == 1:
            return nums[0] * len(requests)
        
        _sum = 0
        presum = [0] * (len(nums))
        
        for val in requests:
            left, right = val
            
            presum[left] += 1
            if right < len(presum) - 1:
                presum[right+1] -= 1
            
        
        for i in range(1, len(presum)):
            presum[i] += presum[i-1]
        
        presum.sort()
        nums.sort()
        
        for i in range(len(nums)):
            _sum += presum[i] * nums[i]
        
        return _sum % 1000000007
        