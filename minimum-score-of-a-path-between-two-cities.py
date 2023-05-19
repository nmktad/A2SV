class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        rep = {i:i for i in range(1,n+1)}
        weight = [1] * (n + 1)

        def find(x):
            if x == rep[x]:
                return x

            rep[x] = find(rep[x])
            return rep[x]

        def union(x, y):
            rx, ry = find(x), find(y)

            if rx != ry:
                if weight[rx] > weight[ry]:
                    rep[ry] = rx
                    weight[rx] += weight[ry]
                else:
                    rep[rx]= ry
                    weight[ry] += weight[rx]

        for cityA, cityB, dis in roads:
            union(cityA, cityB)
        
        ans = float('inf')

        for cityA, cityB, dis in roads:
            if find(cityA) == find(1):
                ans = min(ans, dis)

        return ans