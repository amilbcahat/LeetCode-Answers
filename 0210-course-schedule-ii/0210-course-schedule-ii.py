class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)

        for src, pre in prerequisites:
            preMap[src].append(pre)

        cycle, visited = set(), set()
        topsort = []

        def dfs(crs):
            if crs in cycle:
                return False 

            if crs in visited:
                return True 

            cycle.add(crs)

            for pree in preMap[crs]:
                if not dfs(pree):
                    return False 

            cycle.remove(crs)
            visited.add(crs)
            topsort.append(crs)

            return True 

        for i in range(numCourses):
            if not dfs(i):
                return [] 

        return topsort 
        