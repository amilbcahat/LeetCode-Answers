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
            return [False, p1, p2] 

        if self.rank[p1] < self.rank[p2]: 
            self.par[p1] = p2
        elif self.rank[p2] < self.rank[p1]: 
            self.par[p2] = p1
        else: 
            self.par[p1] = p2
            self.rank[p2] += 1 
        return [True, -1, -1]

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for edge in edges: 
            src, dst = edge
            ans = uf.union(src, dst)
            
        trackEdges = defaultdict(int)
        parToNodes = defaultdict(set)
        edgeCount = 0

        for edge in edges: 
            src, dst = edge
            ans = uf.union(src, dst)
            if not ans[0]: 
                #To note is that, this will always return False, since, we have already run UnionFind and all edges have been connect respectively
                #Belong to same Par
                trackEdges[ans[1]] += 1
                parToNodes[ans[1]].add(src)
                parToNodes[ans[1]].add(dst)

        res = 0
        node_with_edges = 0
        for par, edge_count in trackEdges.items(): 
            k = len(parToNodes[par]) #nodes per parent
            node_with_edges += k
            if edge_count == k * (k - 1) / 2:
                res += 1

        nodes_with_no_edges = (n - node_with_edges) #These are complete as well

        return res + nodes_with_no_edges
        

