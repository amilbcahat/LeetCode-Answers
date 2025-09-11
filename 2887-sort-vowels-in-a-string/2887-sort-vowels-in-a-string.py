class Solution:
    def sortVowels(self, s: str) -> str:
        arr = list(s)
        minHeap = []
        for i,c in enumerate(s): 
            if c in "aeiouAEIOU": 
                arr[i] = ""
                heapq.heappush(minHeap, c)

        for i in range(len(s)): 
            if arr[i] == "":
                arr[i] = heapq.heappop(minHeap)

        return "".join(arr)