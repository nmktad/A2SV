class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        memo = defaultdict(int)

        for i in range(len(nums)):
            for j in range(-500, 500):
                memo[(nums[i], j)] = 1 + memo[(nums[i]-j, j)]

        return max(memo.values())