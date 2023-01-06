from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        _dict = defaultdict(int)
        result = [[], []]
        
        for [winner, loser] in matches:
            _dict[loser] += 1
            _dict[winner] += 0
            
        for key in _dict:
            if _dict[key] == 0:
                result[0].append(key)
            elif _dict[key] == 1:
                result[1].append(key)
        
        return [sorted(result[0]), sorted(result[1])]
            