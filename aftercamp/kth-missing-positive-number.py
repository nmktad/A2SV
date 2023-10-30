class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ans, i = 1, 0

        while k and i < len(arr):
            if ans == arr[i]: i+=1
            else: k-=1

            ans += 1

        return ans - 1 if not k else ans - 1 + k

        