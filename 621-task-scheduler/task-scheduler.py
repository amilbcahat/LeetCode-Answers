class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0
        #We schedule on basis on frequency , and then the idle time , this way we get the minimum time taken for completing these
        #Tasks 
        while maxHeap or q : 
            time += 1 
            #We decrement the cnt (added 1 to decrement the value)
            if maxHeap : 
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt : 
                    #We add cnt , with idle time 
                    q.append([cnt , time + n])
            #If time reaches idle time , we pop the cnt and push back in the heap 
            if q and q[0][1] == time : 
                heapq.heappush(maxHeap , q.popleft()[0])

        return time #Return the time taken 
