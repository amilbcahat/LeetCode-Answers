class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for u, v, t in roads:
            adj_list[u].append((v, t))
            adj_list[v].append((u, t))

        # Let P(n, t) = Number of ways to arrive at intersection n in exactly time t
        # Let T(n) = The shortest time to reach intersction n
        # P(n, T(n)) = Sum for e over edges of n (
        #   P(edge(e), T(n) - time(e)) 
        # )
        # Base case:
        # P(0, 0) = 1
        # P(v, t) = 0 if T(v) != t
        
        START, DEST = 0, n - 1
        shortest_t = [float('inf')] * n
        visited = [False] * n
        pq = [(0, START)]

        while pq:
            t, node = heapq.heappop(pq)
            if visited[node]:
                continue
            visited[node] = True
            shortest_t[node] = t

            for nbr, dt in adj_list[node]:
                heapq.heappush(pq, (t + dt, nbr))
        
        MOD = (10 ** 9) + 7
        dp = {}
        def num_ways(node: int, t: int) -> int:
            if node == 0 and t == 0:
                return 1
            
            if shortest_t[node] != t:
                return 0

            key = node
            if key in dp:
                return dp[key]

            ways = 0
            for nbr, dt in adj_list[node]:
                ways += num_ways(nbr, t - dt)
                ways %= MOD
            
            dp[key] = ways
            return ways

        return num_ways(DEST, shortest_t[DEST])