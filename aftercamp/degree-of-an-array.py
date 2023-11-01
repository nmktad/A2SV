class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = defaultdict(int)
        deg = max(Counter(nums).values())
        ans = inf

        l, r = 0, 0

        while r < len(nums):
            d[nums[r]] += 1

            while d[nums[r]] == deg:
                ans = min(ans, r - l + 1)
                d[nums[l]] -= 1
                l += 1

            r += 1

        return ans    