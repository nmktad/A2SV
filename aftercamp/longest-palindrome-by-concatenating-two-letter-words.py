class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        words = Counter(words)
        flag = False
        
        for w in words:
            if flag and words[w] % 2 and w[0] == w[1]:
                ans += (words[w] - 1) * 2
            else:
                ans += min(words[w], words[w[::-1]]) * 2
                
            if not flag and words[w] % 2 and w[0] == w[1]:
                flag = True

        return ans 
        