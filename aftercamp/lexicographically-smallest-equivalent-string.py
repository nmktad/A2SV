class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        rep = {}

        def find(x):
            if x == rep[x]:
                return x

            rep[x] = find(rep[x])
            return rep[x]

        def union(x, y):
            rx, ry = find(x), find(y)

            if rx != ry:
                if rx < ry:
                    rep[ry] = rx
                else:
                    rep[rx] = ry

        for i in range(len(s1)):
            if s1[i] not in rep:
                rep[s1[i]] = s1[i]
            
            if s2[i] not in rep:
                rep[s2[i]] = s2[i]

            union(s1[i], s2[i])
        
        ans = []

        for char in baseStr:
            if char in rep:
                ans.append(find(char))
            else:
                ans.append(char)

        return ''.join(ans)

            
            
            
            


