class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        rep = {}
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
                    rep[rx]= ry
                    weight[ry] += weight[rx]

        for eq in equations:
            v1 = eq[0]
            op = eq[1:3]
            v2 = eq[-1]

            if v1 not in rep:
                rep[v1] = v1

            if v2 not in rep:
                rep[v2] = v2

            if op == "==":
                union(v1, v2)

        for eq in equations:
            v1 = eq[0]
            op = eq[1:3]
            v2 = eq[-1]

            if v1 in rep and v2 in rep:
                if find(v1) != find(v2) and op == "==" or find(v1) == find(v2) and op == "!=":
                    return False

        return True