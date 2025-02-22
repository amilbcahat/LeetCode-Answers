class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0 

    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2: 
            return False
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        elif self.rank[p2] < self.rank[p1]:
            self.par[p2] = p1
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        
        return True 

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        #Union Find 
        rows = len(grid)
        cols = len(grid[0])
        edges = []
        uf = UnionFind(rows * cols)
        for i in range(rows): 
            for j in range(cols): 
                cur_id = i * cols + j
                if i > 0: 
                    abv_id = (i - 1) * cols + j
                    edges.append((cur_id, abv_id, min(grid[i - 1][j], grid[i][j]))) #capture minweight from this 
                if j > 0: 
                    left_id = i * cols + (j - 1)
                    edges.append((cur_id, left_id, min(grid[i][j - 1], grid[i][j])))

        edges.sort(key = lambda x: -x[2]) #maximized min weight 

        for src, dst, w in edges:
            uf.union(src, dst) # this will union the maximized path first, then once they are connected we return 
            if uf.find(0) == uf.find(rows * cols - 1):
                return w
        
        return 0
        


        #The intuition is that next one should be highest possible minimum value, so we never take not maximized path, because the lower bound of choices is higher 
        # visit = set()
        # minHeap = [(-grid[0][0], 0, 0)]

        # visit = set()
        # minVal = grid[0][0]
        # while minHeap: 
        #     val, i, j = heapq.heappop(minHeap)
        #     minVal = min(minVal, grid[i][j])
        #     if i == rows - 1 and j == cols - 1: 
        #         return minVal

        #     if (i, j) in visit: 
        #         continue

        #     visit.add((i, j))
        #     for r, c in [(i + 1, j), (i, j - 1), (i - 1, j), (i, j + 1)]:
        #         if r >=0 and c >= 0 and r < rows and c < cols: 
        #             heapq.heappush(minHeap, (-grid[r][c], r, c))
