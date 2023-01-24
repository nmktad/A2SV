class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr1 = 0
        ptr2 = len(numbers) - 1
        
        while ptr2 > ptr1:
            if numbers[ptr1] + numbers[ptr2] == target:
                return [ptr1 + 1, ptr2 + 1]
             
            if numbers[ptr1] + numbers[ptr2] > target:
                ptr2 -= 1
            else:
                ptr1 += 1