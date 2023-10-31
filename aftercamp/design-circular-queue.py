class MyCircularQueue:

    def __init__(self, k: int):
        self.st = 0
        self.curr = 0
        self.len = 0
        self.s = [-1] * k
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.len >= self.k: return False
        self.s[self.curr] = value
        self.curr = (self.curr + 1) % self.k
        self.len += 1

        return True

    def deQueue(self) -> bool:
        if self.len == 0: return False

        self.s[self.st] = -1
        self.st = (self.st + 1) % self.k
        self.len -= 1

        return True
        
    def Front(self) -> int:
        return -1 if self.isEmpty() else self.s[self.st]
        
    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.s[(self.st + self.len - 1) % self.k]
        
    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()