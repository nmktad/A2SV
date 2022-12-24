class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left_pointer = n - 1
        rightmost_pointer = m - 1
        leftmost_pointer = m + n - 1
        
        while(left_pointer >= 0):
        
            max_val = 0
            if rightmost_pointer >= 0:
                max_val = max(nums1[rightmost_pointer], nums2[left_pointer])
            else:
                max_val = nums2[left_pointer]
                
            nums1[leftmost_pointer] = max_val
            
            print(max_val, nums1)
            
            if max_val == nums2[left_pointer]:
                left_pointer -= 1
            else:
                rightmost_pointer -= 1
            
            leftmost_pointer -= 1
        
        