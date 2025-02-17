class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        indegree = defaultdict(int)
        adj = defaultdict(list)
        nodes = set()
        for src , dst in relations: 
            adj[src].append(dst)
            nodes.add(src)
            nodes.add(dst)
            indegree[dst] += 1

        queue = deque()

        for n in nodes: 
            if n not in indegree: 
                queue.append(n)

        levels = 0
        node = 0 
        while queue: 
            for i in range(len(queue)): 
                poppedNode = queue.popleft()
                for nei in adj[poppedNode]: 
                    indegree[nei] -= 1
                    if indegree[nei] == 0: 
                        queue.append(nei)
                node += 1
            levels += 1

        return levels if node == len(nodes) else -1 