class Solution:
    def reorganizeString(self, s: str) -> str:
        #This is a preemption algo 
        numCounter = Counter(s)
        maxHeap = []
        for key in numCounter:
            heapq.heappush(maxHeap, (-numCounter[key], key))

        st = ""
        lastAdj = ""
        lastAdjCount = 0
        while maxHeap: 
            #current letter
            cnt1 , ch1 = heapq.heappop(maxHeap)
            #when similar adj what will happen is nothing will be left in maxHeap, so it will move out of this loop 
            if lastAdj and lastAdjCount > 0:
                #last letter now can be adjacent again
                heapq.heappush(maxHeap, (-lastAdjCount, lastAdj)) 
            st += ch1
            cnt1 = -1 * cnt1
            cnt1 -= 1

            #set this as last adj 
            lastAdj = ch1
            lastAdjCount = cnt1 
        print(st)
        return st if len(st) == len(s) else ""
            