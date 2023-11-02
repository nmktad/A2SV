class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return -(min(nums) + k) + max((max(nums) - k), min(nums)+k)
        
        