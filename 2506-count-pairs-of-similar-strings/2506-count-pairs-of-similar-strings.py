from collections import Counter
from collections import defaultdict

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        _dict = defaultdict(int)
        
        for word in words:
            transformed_string = "".join(sorted(Counter(word).keys()))
            
            _dict[transformed_string] += 1
        
        answer = 0
        
        print(_dict)
        
        for val in _dict.values():
            answer += (val * (val - 1)) // 2
            
        return answer