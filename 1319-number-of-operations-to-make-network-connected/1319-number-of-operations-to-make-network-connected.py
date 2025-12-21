class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: 
            return -1 

        adj = defaultdict(list)
        for src, dst in connections:
            adj[src].append(dst)
            adj[dst].append(src)

        visit = set()

        def dfs(node):
            visit.add(node)
            for nei in adj[node]:
                if nei not in visit:
                    dfs(nei)

        x = 0 
        for i in range(n):
            if i not in visit:
                x += 1
                dfs(i)

        return x - 1