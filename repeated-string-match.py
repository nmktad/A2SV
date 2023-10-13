class Solution:
    def repeatedStringMatch(self, s: str, t: str) -> int:
        count = 1
        cp = s
        while cp.find(t) == -1:
            if len(cp) > 2 * max(len(t), len(s)):
                return -1
            count += 1
            cp += s

        return count