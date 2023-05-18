class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rep = {i: i for i in range(len(stones))}
        weight = [1] * len(stones)

        if len(stones) == 1:
            return 0

        isConnected = lambda a, b: a[0] ==  b[0] or a[1] == b[1]

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

        for i in range(len(stones)):
            for j in range(i+1, len(stones)):
                if isConnected(stones[i], stones[j]):
                    union(i, j)

        print(rep)

        ans = defaultdict(int)
        for i in range(len(stones)):
            ans[find(i)] += 1

        finalAns = 0

        for key in ans.values():
            finalAns += key - 1
            
        return finalAns