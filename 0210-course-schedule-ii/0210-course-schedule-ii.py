class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preMap = defaultdict(list)

        for src, dist in prerequisites: 
            preMap[src].append(dist)

        cycle , visited = set(), set()
        topSort = []
        def dfs(src): 
            if src in cycle: 
                return False

            if src in visited: 
                return True

            cycle.add(src)
 
            for nei in preMap[src]:
                if not dfs(nei):
                    return False
            cycle.remove(src)
            visited.add(src)
            topSort.append(src)

            return True 


        for i in range(numCourses): 
            if not dfs(i): 
                return []

        return topSort