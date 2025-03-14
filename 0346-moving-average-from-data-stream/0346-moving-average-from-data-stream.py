class MovingAverage:

    def __init__(self, size: int):
        self.window = deque()
        self.size = size

    def next(self, val: int) -> float:
        self.window.append(val)                                 
        if len(self.window) > self.size:  #could use maxlen parameter that would , ease it to not use popleft everytime
            self.window.popleft()
        return sum(self.window) / len(self.window)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)