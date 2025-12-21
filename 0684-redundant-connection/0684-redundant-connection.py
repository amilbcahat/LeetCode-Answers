class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        indegrees = defaultdict(int)
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
            indegrees[src] += 1 
            indegrees[dst] += 1

        #Kahn's algo
        q = deque()
        for key in indegrees:
            if indegrees[key] == 1:
                q.append(key)

        #Peel leaf nodes
        while q:
            node = q.popleft()
            for nei in adj[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 1:
                    q.append(nei)

        cycle = set()
        for key in range(1, len(edges) + 1):
            if indegrees[key] >= 2: 
                cycle.add(key)

        #Removing last node ensure a single tree
        res = []
        for u, v in edges:
            if u in cycle and v in cycle:
                res = [u, v]

        return res
        


        



