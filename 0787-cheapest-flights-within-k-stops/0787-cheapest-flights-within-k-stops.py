class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = defaultdict(list)

        for s, d, p in flights:
            adj[s].append((d, p))

        minHeap = [(0, src, k + 1)]

        visit = set()
        visited = defaultdict(int)

        while minHeap: 
            cost, node, stops = heapq.heappop(minHeap)

            if node == dst:
                return cost

            if stops <= 0:
                continue 


            if node in visited and visited[node] >= stops: 
                continue 

            
            visited[node] = stops

            for nei,dd in adj[node]:
                heapq.heappush(minHeap, (cost + dd, nei, stops - 1))

        return -1
        # prices = [float("inf")] * n 
        # prices[src] = 0 

        # for i in range(k+1):
        #     #tempArray is used to take the snapshot of x nodes between src and dst and not perform a greedy approach ! 
        #     tmpPrices = prices.copy()
        #     for s , d , p in flights : 
        #         if prices[s] == float("inf"):
        #             continue 
        #         #Starts at root 
        #         if prices[s] + p < tmpPrices[d]:
        #             tmpPrices[d] = prices[s] + p 
        #     prices = tmpPrices 
        
        # return -1 if prices[dst] == float("inf") else prices[dst]

        