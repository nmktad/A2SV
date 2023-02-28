class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        def helper(lptr, rptr):
            if lptr >= rptr:
                return 
            
            s[lptr], s[rptr] = s[rptr], s[lptr]
            
            return helper(lptr + 1, rptr - 1)
        
        helper(0, len(s) - 1)
