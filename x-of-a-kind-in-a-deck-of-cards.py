class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False
        
        count = list(Counter(deck).values())
            
        for i in range(1,len(count)):
            if math.gcd(count[i],count[i-1])<=1:
                return False
        
        return True