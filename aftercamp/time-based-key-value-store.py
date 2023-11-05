class TimeMap:
    def __init__(self):
        self.stampmap = defaultdict(list)
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.stampmap[key].append(timestamp)
        self.map[(key, timestamp)] = value
        
    def get(self, key: str, timestamp: int) -> str:
        if not self.stampmap[key] or timestamp < self.stampmap[key][0]:
            return ''

        found = bisect.bisect_right(self.stampmap[key], timestamp)

        if found >= len(self.stampmap[key]):
            found = len(self.stampmap[key]) - 1

        if self.stampmap[key][found] > timestamp:
            found -= 1

        return self.map[(key, self.stampmap[key][found])]

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)