class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = 0
        num = n & 1

        while x < n.bit_length():
            if n & (1 << x) == num << x:
                num = 0 if num == 1 else 1
                x += 1  
            else:
                return False
        return True