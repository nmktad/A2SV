class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        lptr = 0
        rptr = lptr + 1
        
        window = defaultdict(int)
        
        maxLen = 1
        
        window[s[lptr]] += 1
        
        while rptr < len(s):
            # print("comparing", s[rptr], "in", window)
            if s[rptr] not in window:
                window[s[rptr]] += 1
                rptr += 1
            else:
                window.pop(s[lptr])
                lptr += 1
                
            maxLen = max(maxLen, len(window))
            
        return maxLen