class Solution:
    def reorganizeString(self, s: str) -> str:
        numCounter = Counter(s)
        maxHeap = []
        for key in numCounter:
            heapq.heappush(maxHeap, (-numCounter[key], key))

        st = ""
        lastAdj = ""
        lastAdjCount = 0
        while maxHeap: 
            cnt1 , ch1 = heapq.heappop(maxHeap)
            if lastAdj and lastAdjCount > 0:
                heapq.heappush(maxHeap, (-lastAdjCount, lastAdj)) 
            st += ch1
            cnt1 = -1 * cnt1
            cnt1 -= 1

            lastAdj = ch1
            lastAdjCount = cnt1 
        
        return st if len(st) == len(s) else ""
            