class Solution:
    #Heapify function to maintain heap property.
    def heapify_down(self,arr, n, i):
        l = (2 * i) + 1
        r = (2 * i) + 2
        
        maxVal = i
        
        if l < n and arr[l] > arr[maxVal]:
            maxVal = l
            
        if r < n and arr[r] > arr[maxVal]:
            maxVal = r
            
        if maxVal != i:
           arr[maxVal], arr[i] = arr[i], arr[maxVal]
           self.heapify_down(arr, n, maxVal)
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        p = (n-2) // 2
        
        for i in range(p, -1, -1):
            self.heapify_down(arr, n, i)
        
     
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        
        for i in range(n):
            arr[0], arr[n-i-1] = arr[n-i-1], arr[0]
            self.heapify_down(arr, n-i-1, 0)