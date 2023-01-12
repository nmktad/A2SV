class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        _list = [x for x in range(1, n+1)]
        
        itr = 0
        while len(_list) > 1:
            itr = (itr + k - 1) % len(_list)
            del _list[itr]
            
        return _list[0]