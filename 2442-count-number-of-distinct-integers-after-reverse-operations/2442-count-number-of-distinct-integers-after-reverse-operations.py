class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums = list(map(str, nums))
        
        for i in range(len(nums)):
            nums.append(nums[i][::-1])
        
        nums = set(map(int, nums))
        
        return len(nums)