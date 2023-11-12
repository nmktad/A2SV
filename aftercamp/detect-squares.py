class DetectSquares:
    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        
    def count(self, point: List[int]) -> int:
        ans = 0
        
        for (x, y), n in self.points.items():
            disx, disy = abs(point[0]-x), abs(point[1]-y)

            if disx == disy and disx > 0:
                fcorner = (point[0], y)
                scorner = (x, point[1])
            
                if fcorner in self.points and scorner in self.points:
                    ans += n * self.points[fcorner] * self.points[scorner]
        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)