class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        self.graph = {}

    def checkIn(self, id: int, fr: str, t: int) -> None:
        self.checkin[id] = (fr, t)

    def checkOut(self, id: int, to: str, t: int) -> None:
        fr, et = self.checkin.pop(id)

        if (fr, to) not in self.graph:
            self.graph[(fr, to)] = (t-et, 1)
        else:
            time, count = self.graph[(fr, to)]
            self.graph[(fr, to)] = (time + t - et, count + 1)

    def getAverageTime(self, fr: str, to: str) -> float:
        return self.graph[(fr, to)][0] / self.graph[(fr, to)][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)