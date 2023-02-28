class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def f(arr, rowIndex):
            if len(arr)-1==rowIndex:
                return arr
            temp = [1]
            for i in range(1,len(arr)):
                temp.append(arr[i-1]+arr[i])
            temp.append(1)
        
            return f(temp,rowIndex)
        
        return f([1], rowIndex)
            
            
        
        
        