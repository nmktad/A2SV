from collections import defaultdict

class Solution:
    def printVertically(self, s: str) -> List[str]:
        _dict = defaultdict(list)
        _ans = []
        
        s = s.split()
        
        max_len_word = 0
        
        for val in s:
            max_len_word = max(max_len_word, len(val))
        
        for i in range(len(s)):
            if len(s[i]) < max_len_word:
                s[i] += " " * (max_len_word - len(s[i]))
        
        for i in range(max_len_word):
            for j in range(len(s)):
                if i < len(s[j]):
                    _dict[i].append(s[j][i])      
                
        for val in _dict.values():
            _ans.append(''.join(val).rstrip())
            
        return _ans