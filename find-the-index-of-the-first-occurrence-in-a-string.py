class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle): return -1

        tn = lambda x: ord(x) - ord("a") + 1
        find, look, mod, w = 0, 0, int(1e9) + 7, len(needle)

        for i in range(len(needle)-1, -1, -1):
            find = (find + pow(26, i, mod) * tn(needle[w-i-1])) % mod
            look = (look + pow(26, i, mod) * tn(haystack[w-i-1])) % mod
                    
        if find == look: return 0

        for i in range(w, len(haystack)):
            look = (tn(haystack[i]) + ((look - (tn(haystack[i-w]) * pow(26, w-1, mod))) * 26)) % mod
            
            if find == look: return (i - w) + 1

        return -1