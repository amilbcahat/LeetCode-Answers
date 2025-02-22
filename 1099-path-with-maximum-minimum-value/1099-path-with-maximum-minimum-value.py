class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        visit = set()
        minHeap = [(-grid[0][0], 0, 0)]
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        minVal = grid[0][0]
        while minHeap: 
            val, i, j = heapq.heappop(minHeap)
            minVal = min(minVal, grid[i][j])
            if i == rows - 1 and j == cols - 1: 
                return minVal

            if (i, j) in visit: 
                continue

            visit.add((i, j))
            for r, c in [(i + 1, j), (i, j - 1), (i - 1, j), (i, j + 1)]:
                if r >=0 and c >= 0 and r < rows and c < cols: 
                    heapq.heappush(minHeap, (-grid[r][c], r, c))
