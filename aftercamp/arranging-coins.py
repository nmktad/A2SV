class Solution:
    def arrangeCoins(self, n: int) -> int:
        arr = [1]
        n -= 1

        while n >= arr[-1] + 1:
            n -= arr[-1] + 1
            arr.append(arr[-1] + 1)
  
        return len(arr)