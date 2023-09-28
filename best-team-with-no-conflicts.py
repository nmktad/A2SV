class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = sorted(zip(ages, scores), reverse=True)
        dp = [0] * len(scores)

        ans = 0
        
        for i, [age, score] in enumerate(pairs):
            dp[i] = score
            for j in range(i):
                if score <= pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + score)
            ans = max(ans, dp[i])
        return ans