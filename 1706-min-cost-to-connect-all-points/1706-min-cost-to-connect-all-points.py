class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i : []  for i in range(N)}
        

        for i in range(N):
            x1 , y1 = points[i]
            for j in range(i+1, N):
                x2 , y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[j].append([dist , i])
                adj[i].append([dist, j])


        res = 0 
        visit = set()
        minH = [[0,0]]

        while minH : 
            cur_dist , cur_node = heapq.heappop(minH)
            if cur_node in visit:
                continue 
            visit.add(cur_node)
            res += cur_dist 
            if len(visit) == N : 
                return res 
            for neiDist, nei_node in adj[cur_node]:
                if nei_node not in visit : 
                    heapq.heappush(minH,[neiDist,nei_node])
