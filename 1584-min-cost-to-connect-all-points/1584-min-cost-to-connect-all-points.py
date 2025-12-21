class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #Kruskal with Union find
        N = len(points)
        adj = {i : []  for i in range(N)}

        edges = []
        for i in range(N):
            x1 , y1 = points[i]
            for j in range(i+1, N):
                x2 , y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[j].append([dist , i])
                adj[i].append([dist, j])
                edges.append([j, i, dist])

        print(adj.keys())

        par = list(range(len(adj)))
        edges.sort(key=lambda x: x[2])

        def find(p):
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        e = 0
        total = 0

        for u, v, w in edges: 
            p1, p2 = find(u), find(v)
            if p1 != p2: 
                par[p1] = p2
                total += w
                e += 1 
                if e == N - 1:
                    break 
        return total
                
        