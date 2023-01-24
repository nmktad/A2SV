class Solution: 
    def select(self, arr, i):
        return arr[i]
        
    
    def selectionSort(self, arr,n):
        for i in range(n):
            min_idx = i
            
            for j in range(i, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
                    
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
                    
        return arr
