class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rows, cols = len(isConnected), len(isConnected[0])

        adj = defaultdict(list)
        for i in range(rows):
            for j in range(cols):
                if isConnected[i][j] == 1:
                    adj[i].append(j)
                    adj[j].append(i)


        visit = set()

        def dfs(node):
            visit.add(node)
            for nei in adj[node]:
                if nei not in visit:
                    dfs(nei)

        n = 0 
        for i in range(rows):
            if i not in visit:
                n += 1
                dfs(i)

        return n    
