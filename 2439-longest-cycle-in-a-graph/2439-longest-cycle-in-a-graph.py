class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        adj = defaultdict(list)
        nodes = set()
        for i in range(len(edges)):
            src = i
            dst = edges[src] 
            if dst != -1:
                adj[src].append(dst)
                nodes.add(src)
                nodes.add(dst)

        print(adj)
        visited = set()
        path = set()
        res = -1
        def dfs(node, nodeIndex, lenOfPath):
            nonlocal res
            if node in path:
                res = max(res ,lenOfPath - nodeIndex[node])
                return lenOfPath 

            if node in visited: 
                return -1
            

            path.add(node)
            nodeIndex[node] = lenOfPath
            for adjnode in adj[node]:
                dfs(adjnode, nodeIndex, lenOfPath + 1) 

            path.remove(node)
            visited.add(node)


        for n in nodes: 
            # if n not in indegree: 
            nodeIndex = defaultdict(int)
            print(dfs(n, nodeIndex, 0))

        return res 
        

        