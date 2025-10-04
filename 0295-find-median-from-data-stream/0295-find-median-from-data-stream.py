class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]: 
            heapq.heappush(self.large, num)
        else: 
            heapq.heappush(self.small, -1 * num)

        if len(self.small) > len(self.large) + 1: 
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1: 
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large): 
            return -1 * self.small[0]
        if len(self.large) > len(self.small): 
            return self.large[0]

        return (((-1 * self.small[0]) + self.large[0])) / 2 
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()