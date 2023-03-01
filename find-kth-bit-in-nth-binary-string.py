class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def builder(s, n):
            if n == 0:
                return s

            s += "1" + ''.join('1' if x == '0' else '0' for x in reversed(s))
            
            return builder(s, n - 1)

        return builder("0", n)[k-1]