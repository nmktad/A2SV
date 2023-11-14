from sortedcontainers import SortedList

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        if x == 0: return 0

        res, ans = SortedList(), inf

        for i in range(x, len(nums)):
            res.add(nums[i-x])

            idx = res.bisect_left(nums[i])

            if idx < len(res):
                ans = min(ans,  abs(res[idx] - nums[i]))
            if idx > 0:
                ans = min(ans, abs(res[idx-1] - nums[i]))

        return ans
