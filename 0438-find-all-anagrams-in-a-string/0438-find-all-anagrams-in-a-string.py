class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        
        lptr = 0
        rptr = len(p)
        
        pstr = Counter(p)
        c = Counter(s[:len(p)])
        
        while lptr < len(s) - len(p) + 1:
            if pstr == c:
                ans.append(lptr)
                
            c[s[lptr]] -= 1
            
            if c[s[lptr]] == 0:
                del c[s[lptr]]
            
            lptr += 1
            
            
            if rptr < len(s): 
                c[s[rptr]] += 1
                rptr += 1
            
            
        return ans
            
            