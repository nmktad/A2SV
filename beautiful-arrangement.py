class Solution:
    def countArrangement(self, n: int) -> int:
        nums = [x for x in range(1, n+1)]
        count = 0
        visited = 0

        def validBeauty(arr):
            for i, val in enumerate(arr):
                if val % (i + 1) != 0 and (i + 1) % val != 0:
                    return False
            return True


        def helper(idx, arr):
            nonlocal visited, count
            if len(arr) == len(nums):
                if validBeauty(arr):
                    count += 1
                return

            if idx > len(nums) - 1:
                return

            for i, num in enumerate(nums):
                if not visited & (1 << i):
                    visited |= (1 << i)
                    helper(idx+1, arr+[num])
                    visited &= ~(1 << i)

        helper(0, [])

        return count