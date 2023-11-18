class Solution:
    def intervalIntersection(self, f: List[List[int]], s: List[List[int]]) -> List[List[int]]:
        l, r, ans = 0, 0, []

        while l < len(f) and r < len(s):
            range = [max(f[l][0], s[r][0]), min(f[l][1], s[r][1])]

            if range[0] <= range[1]: ans.append(range)

            if f[l][1] < s[r][1]: l += 1
            else: r += 1

        return ans