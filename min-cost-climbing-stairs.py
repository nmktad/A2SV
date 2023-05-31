class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        dictionary = {}
        def dp(n):
            if n == 0 or n == 1:
                return cost[n]

            if n not in dictionary:
                dictionary[n] = min(dp(n-1), dp(n-2)) + cost[n]

            return dictionary[n]
            
        return dp(len(cost)-1)