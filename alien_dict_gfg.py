class Solution:
    def findOrder(self,alien_dict, N, K):
        graph = defaultdict(list)
        color = defaultdict(int)
        ans = []
        
        alphabet = set(list(alien_dict[0]))
        
        for i in range(len(alien_dict)-1):
            alphabet = alphabet.union(set(list(alien_dict[i+1])))
            
            for j in range(min(len(alien_dict[i]), len(alien_dict[i+1]))):
                if alien_dict[i][j] == alien_dict[i+1][j]:
                    continue
                
                graph[alien_dict[i+1][j]].append(alien_dict[i][j])
                break
            
        def dfs(node):
            if color[node] == 2:
                return True

            elif color[node] == 0:
                color[node] = 1

                if all([dfs(nbr) for nbr in graph[node]]):
                    ans.append(node)
                    color[node] = 2
                    return True

            return False
        
        for letter in alphabet:
            if color[letter] == 0:
                dfs(letter)
        
        return ''.join(ans)