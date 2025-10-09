class Solution:
    def nthUglyNumber(self, n: int) -> int:
        minHeap  = [1]
        seen = set()

        while minHeap and n : 
            cur_ugly = heapq.heappop(minHeap)

            for ugly in [2, 3, 5]: 
                next_ugly = cur_ugly * ugly 
                if next_ugly not in seen:
                    heapq.heappush(minHeap, next_ugly)
                    seen.add(next_ugly)

            n -= 1

        return cur_ugly