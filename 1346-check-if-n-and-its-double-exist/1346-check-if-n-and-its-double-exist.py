class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        for i, val in enumerate(arr):
            ptr = i + 1
        
            while ptr < len(arr):
                print(val)
                if val == 2 * arr[ptr] or arr[ptr] == 2 * val:
                    return True
                ptr += 1
                
        return False
            