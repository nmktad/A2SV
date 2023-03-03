class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        preprod = 1

        for val in nums:
            ans.append(preprod)
            preprod *= val

        suffprod = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= suffprod
            suffprod *= nums[i]
        
        return ans