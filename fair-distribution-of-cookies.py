class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float('inf')
        arr = [0] * k
        cookies.sort(reverse=True)

        def helper(curr, arr):
            nonlocal ans
            # our base case
            if curr > len(cookies) - 1:
                ans = min(ans, max(arr))
                return

            if max(arr) > ans:
                return

            for i in range(len(arr)):
                arr[i] += cookies[curr]
                helper(curr + 1, arr)
                arr[i] -= cookies[curr]

        helper(0, arr)

        return ans