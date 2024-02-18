class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort() #sort by start time 
        available = [i for i in range(n)] #already heapified , since its in increasing order , used for getting minimum free room
        used = [] #(end_time , room)
        count = [0] * n #count[n] = meetins scheduled 

        for start , end in meetings : 
            #Remove the finished meetings , by checking with least finishing meeting first 
            while used and start >= used[0][0]:
                _ , room = heapq.heappop(used)
                heapq.heappush(available , room)

            #if not available rooms , pop once and increase the duration for accounting for waiting 
            if not available : 
                end_time , room = heapq.heappop(used)
                end = end_time + (end - start)
                heapq.heappush(available , room)
            
            room = heapq.heappop(available)
            heapq.heappush(used , (end , room))
            count[room] += 1

        #Returns room number of max 
        return count.index(max(count))

            