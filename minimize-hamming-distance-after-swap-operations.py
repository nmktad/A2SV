class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        rep = {i: i for i in range(len(source))}
        weight = defaultdict(lambda: 1)

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
                    rep[rx] = ry
                    weight[ry] += weight[rx]

        for i, j in allowedSwaps:
            union(i, j)

        representees = defaultdict(list)
        ans = 0

        for i in range(len(source)):
            representees[find(i)].append(i)

        for swapOptions in representees.values():
            count = Counter(list(map(lambda i: source[i], swapOptions)))

            for index in swapOptions:
                if target[index] in count and count[target[index]] != 0:
                    count[target[index]] -= 1
                else:
                    ans += 1
        
        return ans