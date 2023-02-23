class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        _max = float('-inf')

        _sum = sum(nums[:k])
        _max = max(_max, _sum)
        
        for i in range(len(nums) - k):
            _sum = _sum - nums[i] + nums[i+k]
            _max = max(_max, _sum)
            
        return _max/k