class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ranks = {}
        rep = {}

        for point in points:
            rep[tuple(point)] = tuple(point)
            ranks[tuple(point)] = 1

        def find(x):
            if rep[x] == x:
                return x
            rep[x] = find(rep[x])
            return rep[x]
        
        def union(x,y):
            px = find(x)
            py = find(y)

            if px != py:
                if ranks[px] > ranks[py]:
                    rep[py] = px
                    ranks[py] += ranks[px]
                else:
                    rep[px] = py
                    ranks[px] += ranks[py]
        edges = []

        for i in range(len(points)):
            for j in range(i,len(points)):
                weight = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                edges.append((tuple(points[i]),tuple(points[j]),weight))

        edges.sort(key = lambda s:s[2])

        connected = 0
        ans = 0
        for edge in edges:
            u,v,w = edge

            if find(u) != find(v):
                union(u,v)
                ans += w
                connected += 1
            
            if connected == len(points)-1:
                break
        return ans