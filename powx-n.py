class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        pow  = abs(n)

        res = 0

        if pow % 2 == 0:
            res = self.myPow(x * x, pow / 2)
        else:
            res = self.myPow(x * x, (pow - 1) / 2) * x

        return 1/ res if n < 0 else res