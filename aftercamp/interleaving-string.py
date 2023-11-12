class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False

        @cache
        def dp(i, j):
            if i + j == len(s3): return True

            return any([
                i < len(s1) and s1[i] == s3[i+j] and dp(i + 1, j), 
                j < len(s2) and s2[j] == s3[i+j] and dp(i, j + 1)
            ])

        return dp(0,0)