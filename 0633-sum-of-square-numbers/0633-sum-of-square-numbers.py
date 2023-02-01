class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        lptr = 0
        rptr = 1
        
        while rptr >= lptr:
            val = rptr * rptr + lptr * lptr
            
            if val == c or c == 0:
                return 'true'
            elif val > c:
                rptr -= 1
                lptr += 1
            else: 
                rptr += 1
            
            
            
            
                