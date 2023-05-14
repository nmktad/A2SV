class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		color = [0] * V
		
		def dfs(node, parent):
		    
		    if color[node] == 2:
		        return True
		    
		    if color[node] == 0:
    		    color[node] = 1
    		    
    		    for nbr in adj[node]:
    		        if nbr != parent:
    		            if not dfs(nbr,node):
    		                return False
        		            
    		    color[node] = 2
    		    return True
    		    
    	    return False
	    
	    for i in range(V):
	        if color[i] == 0:
	            if not dfs(i,None):
	                return 1
	                
	    return 0