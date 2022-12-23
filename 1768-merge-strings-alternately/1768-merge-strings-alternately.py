class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        
        longest = word1 if len(word1) > len(word2) else word2
        shortest = word1 if len(word1) < len(word2) else word2
            
        for i in range(len(shortest)):
                ans += word1[i] + word2[i]
                
            
        ans += longest[len(shortest):]
        
        return ans
            
                
        
        