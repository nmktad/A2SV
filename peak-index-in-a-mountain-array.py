class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1

        while l <= r:
            m = l + (r - l) // 2

            if arr[m] > arr[m + 1] and arr[m] > arr[m - 1]:
                return m
            if arr[m] < arr[m + 1]:
                l = m + 1
            elif arr[m] < arr[m - 1]:
                r = m - 1