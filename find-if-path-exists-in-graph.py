class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        rep = {i: i for i in range(n)}
        weight = [1] * n

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
                    rep[rb] = ra
                    weight[ra] += weight[rb]
                else:
                    rep[ra] = rb
                    weight[rb] += weight[ra]
        
        return find(source) == find(destination)