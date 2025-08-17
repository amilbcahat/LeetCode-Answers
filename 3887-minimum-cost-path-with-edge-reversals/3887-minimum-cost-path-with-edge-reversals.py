class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src, dst, cost in edges: 
            adj[src].append((dst, cost))
            adj[dst].append((src, cost * 2))

        visit = set()

        minHeap = [(0 , 0)]
        while minHeap:
            nodeCost, node = heapq.heappop(minHeap) 
            if node == n - 1: 
                return nodeCost

            if node in visit: 
                continue

            visit.add(node)
            for nei, c in adj[node]: 
                #dont reverse 
                heapq.heappush(minHeap, (c + nodeCost, nei))

        return -1
                