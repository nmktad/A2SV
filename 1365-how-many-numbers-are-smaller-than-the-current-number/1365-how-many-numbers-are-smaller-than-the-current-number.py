class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for val in nums:
            count = 0
            for num in nums:
                if val > num:
                    count += 1
            ans.append(count)
        
        return ans
            
                