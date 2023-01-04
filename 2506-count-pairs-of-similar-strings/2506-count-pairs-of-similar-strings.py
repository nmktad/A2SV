from collections import defaultdict

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        _dict = defaultdict(int)
        
        for word in words:
            transformed_string = "".join(sorted(set(word)))
            
            _dict[transformed_string] += 1
        
        answer = 0
        
        for val in _dict.values():
            answer += (val * (val - 1)) // 2
            
        return answer