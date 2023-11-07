class Solution:
    def minTimeToType(self, word: str) -> int:
        ptr = "a"
        ans = 0

        for ch in word:
            dist =  abs(ord(ch) - ord(ptr))
            ans += min(26 - dist, dist) + 1
            ptr = ch
            
        return ans
            
        