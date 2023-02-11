class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(idx):
            arr[:idx+1] = reversed(arr[:idx+1])
            
        flips = []
        
        for i in range(len(arr) - 1, 0, -1):
            maxIdx = i
            
            for j in range(i + 1):
                if arr[j] > arr[maxIdx]:
                    maxIdx = j
                    
            if maxIdx != i:
                flip(maxIdx)
                flips.append(maxIdx + 1)
                flip(i)
                flips.append(i+1)
            
        print(arr)
        return flips
                    
            
            