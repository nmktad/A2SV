class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)

        def dfs(itr, cumulative):
            if itr == len(nums):
                if cumulative == target:
                    return 1
                return 0

            if (itr, cumulative) not in memo:
                memo[(itr, cumulative)] = dfs(itr + 1, cumulative + nums[itr]) + dfs(itr + 1, cumulative - nums[itr])
            return memo[(itr, cumulative)]

        return dfs(0, 0)