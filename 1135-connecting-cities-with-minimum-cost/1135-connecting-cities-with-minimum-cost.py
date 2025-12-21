class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        #Prim's algo 
        for src, dst, w in connections:
            adj[src].append((dst, w))
            adj[dst].append((src, w))

        minHeap = []
        for nei, w in adj[1]:
            heapq.heappush(minHeap, (w, nei))

        visit = set()
        visit.add(1)
        total = 0
        while minHeap: 
            weight, node = heapq.heappop(minHeap)

            if node in visit:
                continue

            visit.add(node)
            total += weight

            if len(visit) == n:
                return total

            for ne, c in adj[node]:
                if ne not in visit: 
                    heapq.heappush(minHeap, (c, ne))

        return -1

