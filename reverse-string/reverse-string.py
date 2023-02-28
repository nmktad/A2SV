class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        lptr = 0
        rptr = len(s) - 1
        
        while lptr < rptr:
            s[lptr], s[rptr] = s[rptr], s[lptr]
            lptr += 1
            rptr -= 1
        