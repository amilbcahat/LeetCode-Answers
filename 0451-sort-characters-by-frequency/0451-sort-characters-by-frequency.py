class Solution:
    def frequencySort(self, s: str) -> str:
        maxHeap = [(-val, key) for key, val in Counter(s).items()]
        heapq.heapify(maxHeap)

        s = ""
        while maxHeap: 
            freq, key = heapq.heappop(maxHeap)
            s += (key) * (-1 * freq)

        return s