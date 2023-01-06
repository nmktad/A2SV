class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = []
        
        for col in range(len(grid)):
            rows.append([ x[col] for x in grid])
            
        counter = 0    
        
        for row in grid:
            for col in rows:
                if col == row:
                    counter += 1
                    
        return counter