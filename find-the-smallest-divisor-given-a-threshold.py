class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def checksum(nums, divisor, treshold):
            temp = 0

            for val in nums:
                temp += ceil(val/divisor)

            return temp <= threshold

        lptr = 1
        rptr = max(nums)
        ans = None

        while lptr <= rptr:
            mid = lptr + (rptr - lptr) // 2

            if checksum(nums, mid, threshold):
                ans = mid
                rptr = mid - 1
            else:
                lptr = mid + 1

        return ans