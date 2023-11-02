class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = days[-1]
        dp = [0 for i in range(n+1)]
        days = set(days)

        for i in range(1, n+1):
            dp[i] = inf
            for dur, cost in zip([1, 7, 30], costs):
                if i not in days: dp[i] = dp[i-1]
                else: dp[i]= min(dp[i], dp[max(0,i-dur)] + cost)

        return dp[-1]



        