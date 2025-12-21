class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        for src, pre in prerequisites: 
            adj[src].append(pre)

        visited = set()
        def dfs(node):
            if node in visited:
                return False 

            if adj[node] == [ ]: 
                return True 

            visited.add(node)

            for nei in adj[node]:
                if not dfs(pre):
                    return False 

            visited.remove(node)

            adj[node] = []
            return True 

        for i in range(numCourses):
            if not dfs(i):
                return False 

        return True 

            