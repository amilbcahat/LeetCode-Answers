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
        
        if self.rank[p1] > self.rank[p2]: 
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]: 
            self.par[p1] = p2
        else: 
            self.par[p2] = p1
            self.rank[p1] += 1
        
        return True

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        uf = UnionFind(n)

        for s, d, w  in edges:
            uf.union(s, d)

        #Intuition is that AND never gets bigger than the smallest number ANDed from , so we simple consider all the edges, when picking the cost for a component, 
        #If they belong in the same, then just get cost by ANDing all the edges 
        component_cost = {}
        for u, v, w in edges: 
            root = uf.find(u)
            if root not in component_cost: 
                component_cost[root] = w
            else: 
                component_cost[root] &= w

        res = []
        for start, end in query:
            p1, p2 = uf.find(start), uf.find(end)
            if p1 == p2:
                #Answer is definitely there 
                res.append(component_cost[p1])
            else: 
                res.append(-1)
            
        return res