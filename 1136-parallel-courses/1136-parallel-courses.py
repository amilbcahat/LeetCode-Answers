class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        #kahns algo for topo sort 
        adj = defaultdict(list)
        indegree = defaultdict(int)
        nodes = set()
        for src, dst in relations :
            nodes.add(src)
            nodes.add(dst)
            adj[src].append(dst)
            indegree[dst] += 1

        queue = deque()
        for u in nodes:
            if u not in indegree:
                queue.append(u)

        node = 0 
        levels = 0 
        while queue:
            for i in range(len(queue)):
                ne = queue.popleft()
                for nei in adj[ne]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)
                node += 1

            levels += 1
            
        return levels if node == len(nodes) else -1 