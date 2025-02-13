class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        maxStartHeap = []
        maxEndHeap = []
        for i in range(len(intervals)):
            heapq.heappush(maxStartHeap, (-intervals[i][0], i))
            heapq.heappush(maxEndHeap, (-intervals[i][1], i))

        res = [0] * len(intervals)
        for _ in range(n):
            topEnd, endIndex = heapq.heappop(maxEndHeap)
            res[endIndex] = -1 
            if maxStartHeap and -maxStartHeap[0][0] >= -topEnd: 
                topStart, startIndex = heapq.heappop(maxStartHeap)
                while maxStartHeap and -maxStartHeap[0][0] >= -topEnd: 
                    topStart, startIndex = heapq.heappop(maxStartHeap)
                res[endIndex] = startIndex 
                heapq.heappush(maxStartHeap, (topStart, startIndex))

        return res