class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #With Queue
        adj = defaultdict(list)

        for src, dst, w in times:
            adj[src].append((dst, w))

        # print(adj)

        minHeap = [(0, k)] #node, dist so far

        visit = set()
        while minHeap: 
            di, node = heapq.heappop(minHeap)

            if node in visit:
                continue 

            visit.add(node)

            # print(node, di )
            if len(visit) == n:
                return di

            for nei, d in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, (di + d, nei))

        # print(visit)
        return -1




