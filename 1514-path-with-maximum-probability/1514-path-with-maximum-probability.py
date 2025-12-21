class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adj = defaultdict(list)
        for i , (src , dst) in enumerate(edges):
            adj[src].append((succProb[i] , dst))
            adj[dst].append((succProb[i] , src))

        #This minus -1 , is used because we are multiplying here , if 0 taken , that would make every product 0 , hence mess up the traversal 
        #minus 1 is taken instead of 1 , because , it will change all product values to -1 , making it as maxHeap 
        maxHeap = [(-1 , start_node)]
        
        shortest = {}

        while maxHeap : 
            p1 , n1 = heapq.heappop(maxHeap)

            if n1 == end_node : 
                print(shortest)
                #Then we fix the value and return the answer ! 
                return -p1

            if n1 in shortest : 
                continue 

            shortest[n1] = p1

            for p2 , n2 in adj[n1]:
                if n2 not in shortest :
                    heapq.heappush(maxHeap , (p1 * p2 , n2))
        
        return 0