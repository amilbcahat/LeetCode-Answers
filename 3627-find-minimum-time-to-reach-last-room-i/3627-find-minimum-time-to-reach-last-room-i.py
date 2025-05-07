class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rows, cols = len(moveTime), len(moveTime[0])
        minHeap = [[0, 0, 0]]
        di = [[0, -1], [-1, 0], [1, 0], [0, 1]]
        cost = 0 
        visited = set()
        while minHeap: 
            time, r, c = heapq.heappop(minHeap)

            if r == rows - 1 and c == cols - 1: 
                return time

            if (r, c) in visited: 
                continue 

            visited.add((r, c))

            for dr, dc in di: 
                r1 = r + dr
                c1 = c + dc
                
                if r1 >= 0 and r1 < rows and c1 >= 0 and c1 < cols: 
                    timeNeeded = moveTime[r1][c1]
                    nextArrivalTime = time
                    heapq.heappush(minHeap, [max(timeNeeded, nextArrivalTime) + 1, r1, c1])

        return -1
