class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = [[0 for i in range(len(grid) - 2)] for j in range (len(grid) - 2)]
        
        for i in range(len(ans)):
            for j in range(len(ans[0])):
                _max = 0
                
                for xitr in range(i, i+3):
                    for yitr in range(j, j+3):
                        _max = max(_max, grid[xitr][yitr])
                
                ans[i][j] = _max
            
        return ans