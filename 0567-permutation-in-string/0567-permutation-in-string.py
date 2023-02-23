class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowlen = len(s1)
        s1 = Counter(s1)
        window = Counter(s2[:windowlen])
        
        lptr = 0
        rptr = windowlen
        
        while rptr <= len(s2):
            if window == s1:
                return True
            else:
                print(window)
                window[s2[lptr]] -= 1
                
                if window[s2[lptr]] == 0:
                    del window[s2[lptr]]
                
                lptr += 1
                
                if rptr < len(s2): 
                    window[s2[rptr]] += 1
                
                rptr += 1