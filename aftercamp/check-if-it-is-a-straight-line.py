class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        x1, y1 = c[0][0], c[0][1]

        def calcslope(x2,y2):
            return (y2-y1) / (x2-x1) if (x2-x1) != 0 else None

        slope = calcslope(c[1][0], c[1][1])

        for i in range(1,len(c)):  
            if slope != calcslope(c[i][0],c[i][1]): return False
        
        return True
