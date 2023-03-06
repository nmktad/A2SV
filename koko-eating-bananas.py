class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def findtime(m, h, arr):
            ans = 0

            for val in arr:
                if val <= m:
                    ans += 1
                else: 
                    ans += ceil(val/m)

            return ans <= h

        l = 1
        r = max(piles)
        a = float('inf')

        while l <= r:
            m = l + (r - l) // 2

            if findtime(m, h, piles):
                a = m
                r = m - 1
            else:
                l = m + 1

        return a