class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        #Simple BFS 
        #Make adjacency list with indicies
        adj = defaultdict(list)
        for i , n in enumerate(manager):
            adj[n].append(i)

        q = deque([(headID ,0)])

        print(adj)
        maxTime = float("-inf")
        while q : 
            node, time = q.popleft()

            print(node , time)
            #Max time taken because , we needed to ensure that all employees have been alerted !
            maxTime = max(maxTime , time)
            
            for nei in adj[node]:
                q.append((nei , time + informTime[node]))

        return maxTime 
            