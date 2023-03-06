class Solution:
    def mySqrt(self, x: int) -> int:
        l  = 0
        r = x
        ans = 0

        while l <= r:
            m = l + (r - l) // 2

            if m * m < x:
                ans = max(ans, m)
                l = m + 1
            elif m * m > x:
                r = m - 1
            else:
                return m
                
        return ans