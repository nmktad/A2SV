class Solution:
    def maxArea(self, height: List[int]) -> int:
        lptr = 0
        rptr = len(height) - 1
        
        _max = float('-inf')
        
        while lptr <= rptr :
            y = min(height[lptr], height[rptr])
            x = rptr - lptr
            
            _max = max(x*y, _max)
            
            if height[lptr] > height[rptr]:
                rptr -= 1
            else:
                lptr += 1
                
        return _max
        
        
        