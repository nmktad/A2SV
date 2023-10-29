class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4275: return 1

        @cache
        def helper(s1, s2):
            if s1 == 0 and s2 == 0: return 1/2
            
            if s1 == 0: return 1
            
            if s2 == 0: return 0

            ans = 0

            for i in range(4):
                ans += (1/4) * helper(max(0, s1-(100 - (i * 25))), max(0, s2-(i * 25))) 

            return ans

        return helper(n, n)