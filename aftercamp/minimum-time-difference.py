class Solution:
    def findMinDifference(self, tp: List[str]) -> int:
        n = len(tp)
        for i in range(n):
            tp[i] = list(map(int, tp[i].split(":")))

        tp.sort()

        ans = inf

        for i in range(n - 1):
            idx = i + 1
            poss = (tp[idx][0] - tp[i][0]) * 60 + (tp[idx][1] - tp[i][1])
            ans = min(ans, poss)

        poss = (tp[-1][0] - tp[0][0]) * 60 + tp[-1][1]-tp[0][1]
        ans = min(ans, min((24 * 60) - poss, poss))

        return ans