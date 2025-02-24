class Solution:
    def nthUglyNumber(self, n: int) -> int:
        minHeap = [1]
        seen = set()

        for _ in range(n): 
            cur_ugly = heapq.heappop(minHeap)

            for cur_p in [2 , 3, 5]: 
                next_ugly = cur_p * cur_ugly
                if next_ugly not in seen:
                    heapq.heappush(minHeap, next_ugly)
                    seen.add(next_ugly)

        return cur_ugly