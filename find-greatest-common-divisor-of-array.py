class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxNum = minNum = nums[0]

        for val in nums:
            maxNum = max(val, maxNum)
            minNum = min(val, minNum)

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        return gcd(maxNum, minNum)