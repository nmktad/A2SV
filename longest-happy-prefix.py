class Solution:
    def longestPrefix(self, s: str) -> str:
        lhp = [0] * len(s)
        prevLhp, i = 0, 1

        while i < len(s):
            if s[i] == s[prevLhp]:
                lhp[i] = prevLhp + 1
                prevLhp += 1
                i += 1
            elif prevLhp > 0:
                prevLhp = lhp[prevLhp-1]
            else:
                i += 1
        
        return s[:prevLhp]