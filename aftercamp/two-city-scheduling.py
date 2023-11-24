class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans = sum([i for i, _ in costs])

        costs = sorted([(j - i, i, j) for i, j in costs])

        for i in range(len(costs)//2):
            ans -= costs[i][1]
            ans += costs[i][2]
        return ans
        