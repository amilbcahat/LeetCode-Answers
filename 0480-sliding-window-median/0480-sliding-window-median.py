class MedianFinder:
    def __init__(self):
        self.small , self.large = [], []

    def remove(self, num):
        if self.small and num <= -1 * self.small[0]:
            self.remove_helper(self.small, -num)
        elif self.large and num >= self.large[0]:
            self.remove_helper(self.large, num)
        self.rebalance()
            
    def remove_helper(self, heap, num):
        ind = heap.index(num)
        heap[ind] = heap[-1]
        del heap[-1]

        if ind < len(heap):
            heapq._siftup(heap, ind) #Restore Heap Property Upward
            heapq._siftdown(heap, 0, ind) #Restore Heap Property Downwarss

    def insert(self , num):
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else: 
            heapq.heappush(self.small, -1 * num)

        self.rebalance()

    def rebalance(self):
        if len(self.small) > len(self.large) + 1: 
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
    
    def getMedian(self):
        if len(self.small) > len(self.large): 
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        return ( -1 * self.small[0] + self.large[0]) / 2

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        client = MedianFinder()
        for i in range(k): 
            client.insert(nums[i])
        
        res = []
        res.append(client.getMedian())
        
        l = 0
        for r in range(k, len(nums)): 
            client.insert(nums[r])
            client.remove(nums[l])
            print(client.getMedian())
            res.append(client.getMedian())
            l += 1
        
        return res