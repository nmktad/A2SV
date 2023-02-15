class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)
        i = 0
        
        for val in (nums[len(nums) - k:] + nums[:len(nums) - k]):
            nums[i] = val
            i+=1