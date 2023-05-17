class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rep = {i: i for i in range(1, len(edges) + 1)}
        weight = [1] * (len(edges) + 1)
        ans = None

        def find(x):
            if rep[x] == x:
                return x

            rep[x] = find(rep[x])
            return rep[x]
        
        for a,b in edges:
            ra = find(a)
            rb = find(b)

            if ra != rb:
                if weight[ra] > weight[rb]:
                    rep[ra] = rb
                    weight[ra] += weight[rb]
                else:
                    rep[rb] = ra
                    weight[rb] += weight[ra]
            else:
                ans = [a, b]
        
        return ans