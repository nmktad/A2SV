class MyHashMap:
    def __init__(self):
        self.map = [None] * int(1e6 + 1)        

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        if self.map[key] == None:
            return -1

        return self.map[key]
        
    def remove(self, key: int) -> None:
        self.map[key] = None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)