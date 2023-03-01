class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        res = self.myPow(x * x, abs(n) / 2) if abs(n) % 2 == 0 else self.myPow(x * x, (abs(n) - 1) / 2) * x

        return res if n >= 0 else 1/res