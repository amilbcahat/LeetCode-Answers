class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for s, d, w in roads: 
            adj[s].append((d, w))
            adj[d].append((s, w))

        minHeap = [(0, 0)]

        MOD = 10 ** 9 + 7 

        visit = set()
        min_cost = [float("inf")] * n 
        path_count = [0] * n 
        path_count[0] = 1

        while minHeap: 
            cur_cost, cur_node = heapq.heappop(minHeap)
                
            for nei, nei_cost in adj[cur_node]: 
                #Here we are not traversing , each and every node
                #When we only push those nodes to heap, which we know , are min_cost 
                if nei_cost + cur_cost < min_cost[nei]: 
                    min_cost[nei] = nei_cost + cur_cost 
                    path_count[nei] = path_count[cur_node]
                    heapq.heappush(minHeap, (min_cost[nei], nei))
                elif nei_cost + cur_cost == min_cost[nei]: 
                #Otherwise we simply calculate, instead of traversing and increasing the TE for them 
                    path_count[nei] = (path_count[nei] + path_count[cur_node]) % MOD
        
        return path_count[n - 1]
