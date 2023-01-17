class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            j = i+1
            
            while j < len(heights):
                if heights[i] < heights[j]:
                    heights[i], heights[j] = heights[j], heights[i]
                    names[i], names[j] = names[j], names[i]
                
                j += 1
        
        return names
        