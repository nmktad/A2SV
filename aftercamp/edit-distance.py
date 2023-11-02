class Solution:
    def minDistance(self, w: str, w2: str) -> int:
        @cache
        def helper(i, j):
            if i == len(w):
                return len(w2) - j

            if j == len(w2):
                return len(w) - i

            if w[i] == w2[j]:
                return helper(i+1, j+1)

            return 1 +  min(helper(i+1, j+1), helper(i+1, j), helper(i, j+1))

        return helper(0, 0)