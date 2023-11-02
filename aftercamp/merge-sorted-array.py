class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        lptr = n - 1
        rmptr = m - 1
        lmptr = m + n - 1
        
        while lptr >= 0:
            mval = 0

            if rmptr >= 0:
                mval = max(nums1[rmptr], nums2[lptr])
            else:
                mval = nums2[lptr]
                
            nums1[lmptr] = mval
            
            if mval == nums2[lptr]:
                lptr -= 1
            else:
                rmptr -= 1
            
            lmptr -= 1
        
        