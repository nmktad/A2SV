class RandomizedSet:

    def __init__(self):
        self.li = []
        self.pos = {}
        
    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        
        self.li.append(val)
        self.pos[val] = len(self.li) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        
        tbr = self.pos[val]
        self.pos[self.li[-1]] = self.pos[val]
        self.li[tbr], self.li[-1] = self.li[-1], self.li[tbr]
        self.li.pop()

        del self.pos[val]
        return True
    def getRandom(self) -> int:
        return random.choice(self.li)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()