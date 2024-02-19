class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        #Same as Meetings 3 problem 
        weightMap = defaultdict(int)
        #Mapping index to the server weight !
        for i , n in enumerate(servers):
            weightMap[i] = n 
        
        used = [] #(end_time , indexOfServer) end_time -> We track the end_time of each task 
        available = [(n , i) for i , n in enumerate(servers)] #(weight , index)
        #heapify with respect to weight and then with respect to index 
        heapq.heapify(available)
        ans = []

        t = 0 
        for curTime , dt in enumerate(tasks) : 
            #Finish the used up tasks , if the task time gets over 
            #Then push the server to available servers 
            #We match , and pop up curTime tasks holding server(multiple tasks can be assigned at same time)
            #Many Servers at some time (curTime) can be freed , we pop up all those servers 
            while used and curTime == used[0][0]:
                _ ,weightOfS ,indexOfServer = heapq.heappop(used)
                heapq.heappush(available , (weightOfS, indexOfServer))

            #if no available 
            if not available : 
                #We here , have to wait so that the server could complete their task , but 
                #to code nicely , we just pop from used server
                #And jump the time counter to the end time of the latest server task 
                #Push that latest server onto avaialble servers
                #and set the time to end_time of the previous task of this server ! 
                end_time , weightOfS ,indexOfServer = heapq.heappop(used)
                curTime = end_time
                heapq.heappush(available , (weightOfS, indexOfServer))

            #If available servers , then pop available server and push to used server, to indicate
            #that the server is being currently used  
            #Assign the current task (current task can be assigned to only one server)
            weightOfS, indexOfS = heapq.heappop(available)
            heapq.heappush(used , (curTime + dt ,weightOfS, indexOfS))
            #Set the answer array as necessary
            ans.append(indexOfS)
        return ans 

        

