class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rows, cols = len(moveTime), len(moveTime[0])
        visited = set()
        di = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        minHeap = [[0, 0, 0, 1]]

        while minHeap: 
            time, r, c, useOne = heapq.heappop(minHeap)

            if r == rows - 1 and c == cols - 1: 
                return time 

            if (r, c) in visited: 
                continue

            visited.add((r, c))

            for dr, dc in di: 
                nr = r + dr
                nc = c + dc 
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols: 
                    minTime = moveTime[nr][nc]
                    nextArrivalTime = time
                    useThisTime = max(minTime, nextArrivalTime) + useOne
                    heapq.heappush(minHeap, (useThisTime, nr, nc, 2 if useOne == 1 else 1))

        
        return -1 
                


