class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        nums = sorted(set(nums))
        
        for lptr, num in enumerate(nums):
            r = num + n - 1
            rptr = bisect_right(nums, r)
            ans = min(ans, n - (rptr-lptr))
        return ans