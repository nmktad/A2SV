class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for val in nums:
            ans ^= val

        return ans

        



        
        