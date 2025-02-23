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
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key= lambda x: x[2]) 
        queries_with_index = []
        for i, (p, q, limit) in enumerate(queries): 
            queries_with_index.append((limit, p, q, i))

        queries_with_index.sort(key= lambda x: x[0])

        uf= UnionFind(n)
        #Because after sorting we did not knew where to put for that result !!
        ans = [False] * len(queries)
        edges_index = 0
        for limit, p, q, i in queries_with_index: 
            while edges_index < len(edgeList) and edgeList[edges_index][2] < limit: 
                src = edgeList[edges_index][0]
                dst = edgeList[edges_index][1]
                uf.union(src, dst)
                edges_index += 1 
            
            ans[i] = (uf.find(p) == uf.find(q))

        return ans
