class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        
        _max = -1
        
        ans = [0] * len(arr)    
        
        for i in range(len(arr)-1, -1, -1):
            ans[i] = _max
            _max = max(_max, arr[i])
            
        return ans
            
            
            
                
            
                
        