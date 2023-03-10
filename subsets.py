class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def helper(arr, curr):
            if curr > len(nums) - 1:
                ans.append(arr)
                return

            helper(arr, curr + 1)
            helper(arr + [nums[curr]], curr + 1)

        helper([], 0)

        return ans