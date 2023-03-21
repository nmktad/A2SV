class Solution:
    def splitString(self, s: str) -> bool:
        def helper(start, arr):
            if start == len(s) and len(arr) >= 2:
                return True

            for i in range(start, len(s)):
                if not arr or arr[-1] - int(s[start: i+1]) == 1:
                    found = helper(i+1, arr+[int(s[start: i+1])])

                    if found:
                        return True

        return helper(0, [])