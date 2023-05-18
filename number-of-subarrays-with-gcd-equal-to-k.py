class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            if b == 0:
                return a

            return gcd(b, a % b)

        count = 0

        for i in range(len(nums)):
            subarr = nums[i]

            for j in range(i, len(nums)):
                subarr = gcd(subarr, nums[j])
                if subarr == k:
                    count += 1

        return count