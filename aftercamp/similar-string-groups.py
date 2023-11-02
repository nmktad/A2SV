class Solution:
    def numSimilarGroups(self, s: List[str]) -> int:
        rep = {i: i for i in range(len(s))}

        def find(x):
            if rep[x] != x:
                rep[x] = find(rep[x])
            
            return rep[x]

        def union(x, y):
            rx, ry = find(x), find(y)

            if rx != ry:
                rep[rx] = ry
        
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                c = 0
                for k in range(len(s[i])):
                    if s[i][k] != s[j][k]:
                        c += 1

                if c <= 2:
                    union(i, j)

        visited = set()

        for i in range(len(s)):
            visited.add(find(i))
        
        return len(visited)
                
        

                

        

                            

                    
                    
                    
                    



                    



            

        

        