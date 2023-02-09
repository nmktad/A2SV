class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        rptr = len(piles) - 2
        lptr = 0
        
        ans = 0
        
        while rptr > lptr:
            ans += piles[rptr]
            rptr -= 2
            lptr += 1
        
        return ans