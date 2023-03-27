class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def returnCount(mid, arr):
            count = 0
            for val in arr:
                count = count + 1 if val <= mid else count
            return count

        left = 1
        right = len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2

            if returnCount(mid, nums) > mid:
                right = mid
            else:
                left = mid + 1
        
        return left