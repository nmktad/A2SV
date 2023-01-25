class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        _max = arr[0]
        _maxptr = 0
        
        for i, val in enumerate(arr):
            if val > _max:
                _max = val
                _maxptr = i
                
        if _maxptr == 0 or _maxptr == len(arr) - 1:
            return False
                
        for i in range(0, _maxptr):
            if arr[i] >= arr[i+1]:
                return False
        
        for i in range(_maxptr, len(arr) - 1):
            if arr[i] <= arr[i+1]:
                return False
            
        return True
            