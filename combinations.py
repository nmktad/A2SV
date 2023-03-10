class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def helper(curr, arr):
            if curr > n + 1:
                return

            if len(arr) == k:
                ans.append(arr.copy())
                return

             

            
            arr.append(curr)
            helper(curr + 1, arr)
            arr.pop()
            helper(curr + 1, arr)

        helper(1, [])

        return ans