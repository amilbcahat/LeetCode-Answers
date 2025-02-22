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
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        #Djishktra Algo 
        minHeap = [(0, 0, 0)]
        rows = len(heights)
        cols = len(heights[0])
        visited = set()
        while minHeap: 
            max_diff, i, j = heapq.heappop(minHeap) #minimized maxDiff
            if i == rows - 1 and j == cols - 1: 
                return max_diff

            if (i, j) in visited:
                continue
            
            visited.add((i , j))

            for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if r >= 0 and c >= 0 and c < cols and r < rows: 
                    diff = abs(heights[i][j] - heights[r][c])
                    heapq.heappush(minHeap, (max(max_diff, diff), r, c))


        # Union Find 
        # rows = len(heights)
        # cols = len(heights[0])
        # uf = UnionFind(rows * cols)
        # #Change matrix to 1D for better Union Find (consider index to index as node)
        # #Then do union find, keeping weight
        # #Sort edges with weight 
        # #Then union those weights
        # #If parent of any node is from root to last node, then path is there 
        # #Since Path is from minimum weighted edge, it is clear that this is the minimum effort path 
        # edges = []
        # for i in range(rows): 
        #     for j in range(cols): 
        #         cur_id = i * cols + j 
        #         if i > 0: 
        #             #above id
        #             abv_id = (i - 1) * cols + j 
        #             edges.append((cur_id, abv_id, abs(heights[i][j] - heights[i - 1][j])))
        #         if j > 0: 
        #             #left if 
        #             left_id = i * cols + (j - 1)
        #             edges.append((cur_id, left_id, abs(heights[i][j - 1] - heights[i][j])))
        
        # edges.sort(key = lambda x: x[2])
        # #Sort by weight
        # for src, dst, diff in edges: 
        #     uf.union(src, dst)
        #     if uf.find(0) == uf.find(rows * cols - 1): 
        #         return diff 

        # return 0 
        