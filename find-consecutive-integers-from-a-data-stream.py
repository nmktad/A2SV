class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.val = value
        self.cap = k
        self.count = 0

    def consec(self, num: int) -> bool:
        if len(self.queue) < self.cap - 1:
            self.count += self.val != num
            self.queue.append(self.val == num)
            return False

        self.count += self.val != num
        self.queue.append(self.val == num)

        if self.count:
            if not self.queue.popleft():
                self.count -= 1
            
            return False          

        return self.queue.popleft()
        




        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)