class Solution:
    def frequencySort(self, s: str) -> str:
        countMap = Counter(s)

        minHeap = []
        for item , val in countMap.items():
            heapq.heappush(minHeap , (-val , item))

        res = ""
        
        while len(minHeap):

            multiplier, poppedElem  = heapq.heappop(minHeap)
            print(poppedElem , multiplier)
            res += poppedElem * (multiplier * -1)
        
        return res 