class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        #Prims Algo to find Min spanning tree -> 
        adj = defaultdict(list)

        for src, dst, w in connections: 
            adj[src].append((dst, w))
            adj[dst].append((src, w))

        minHeap = []
        for nei, weight in adj[1]:
            heapq.heappush(minHeap, [weight, 1, nei])

        visit = set()
        visit.add(1)

        total = 0
        while minHeap: 
            w, n1, n2 = heapq.heappop(minHeap)

            if n2 in visit: 
                continue 

            total += w

            visit.add(n2)

            if len(visit) == n:
                return total

            for nei, w in adj[n2]: 
                if nei not in visit: 
                    heapq.heappush(minHeap, [w, n2, nei])

        return -1
