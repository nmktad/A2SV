# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, arr: 'MountainArray') -> int:
        l, r, peak = 0, arr.length()-1, 0

        while l < r:
            peak = l + (r-l) // 2

            if arr.get(peak) < arr.get(peak + 1):
                l = peak + 1
            else:
                r = peak

        peak = l

        l, r = 0, peak

        while l <= r:
            m = l + (r-l)//2
            curr = arr.get(m)

            if curr == target:
                return m
            
            if curr > target:
                r = m - 1
            else:
                l = m + 1

        l, r = peak + 1, arr.length() - 1

        while l <= r:
            m = l + (r-l) // 2
            curr = arr.get(m)

            if curr == target:
                return m
            
            if curr > target:
                l = m + 1
            else:
                r = m - 1
        
        return -1