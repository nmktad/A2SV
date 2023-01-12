class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter = [[0]*26 for _ in range(len(words))]
        ans = []

        for row, word in enumerate(words):
            offset = ord('a')
            for char in word:
                _ascii = ord(char)
                counter[row][_ascii - offset] += 1
                
        for i in range(26):
            _min = float('inf')
            for val in counter:
                _min = min(_min, val[i])
            
            for _ in range(_min):
                ans.append(chr(i + ord('a')))
        
        return(ans)
                
            
            