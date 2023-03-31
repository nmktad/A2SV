class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = 0

        def helper(idx, arr):
            nonlocal visited
            if len(arr) == len(nums):
                ans.append(arr)
                return

            if idx > len(nums) - 1:
                return

            for i, num in enumerate(nums):
                if not visited & (1 << i):
                    visited |= (1 << i)
                    helper(idx+1, arr+[num])
                    visited &= ~(1 << i)

        helper(0, [])

        return ans