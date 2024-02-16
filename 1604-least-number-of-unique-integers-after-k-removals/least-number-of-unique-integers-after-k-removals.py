class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        countMap = Counter(arr)

        minHeap = []
        for key , val in countMap.items():
            heapq.heappush(minHeap , (val , key))

        while minHeap and k > 0 :
            #Remove the lesser freq first , if k is greater , remove it all 
            if k >= minHeap[0][0] :  
                freq , elem = heapq.heappop(minHeap)
                print(freq , elem)
                k -= freq 
            else: 
            #else this elem would be considered in final answer , so include it !
                break #

        print(minHeap)
        return len(minHeap)