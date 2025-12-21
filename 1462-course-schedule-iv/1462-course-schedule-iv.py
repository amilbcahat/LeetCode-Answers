class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adj = defaultdict(list)

        for src, dst in prerequisites: 
            adj[src].append(dst)
        
        def dfs(node):
            if node == target: 
                return True 

            visit.add(node)

            res = False 
            for nei in adj[node]:
                if nei not in visit:
                    res = res or dfs(nei)

            return res

        res = []
        for s, target in queries:
            visit = set()
            res.append(dfs(s))

        return res

            

        

