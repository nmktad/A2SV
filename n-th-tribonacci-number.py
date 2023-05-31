class Solution:
    def tribonacci(self, n: int) -> int:
        dictionary = {}

        def tri(n):
            if n == 0 or n == 1:
                return n

            if n == 2:
                return 1

            if n not in dictionary:
                dictionary[n] = tri(n-1) + tri(n-2) + tri(n-3)

            return dictionary[n]

        return tri(n)