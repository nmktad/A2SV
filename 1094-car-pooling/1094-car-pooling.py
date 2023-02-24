class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        path = [0] * (max([trip for singletrip in trips for trip in singletrip]) + 1)
        
        for trip in trips:
            num, _from, to = trip
            
            path[_from + 1] += num
            
            if to < len(path) - 1:
                path[to + 1] -= num
                
        for i in range(1, len(path)):
            path[i] += path[i-1]
        
        print(path)
        
        if max(path) <= capacity:
            return True
        else:
            return False