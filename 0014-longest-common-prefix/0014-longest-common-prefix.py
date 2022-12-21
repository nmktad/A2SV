class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = len(strs[0])
        shortestWord = ""
        ans = ""
        
        for word in strs:
            if len(word) <= shortest:
                shortest = len(word)
                shortestWord = word
                
        print(shortestWord)
        
        for index, char in enumerate(shortestWord):
            counter = 0
            for word in strs:
                if word[index] == char:
                    counter += 1
            
            if counter == len(strs):
                ans += char
            else:
                break
        
        
        return ans
            
        
            
        

                
            