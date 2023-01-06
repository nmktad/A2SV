class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        
        for i in range(len(nums)):
            ans.append([nums[nums[i]]])
        
        return [item for sublist in ans for item in sublist]