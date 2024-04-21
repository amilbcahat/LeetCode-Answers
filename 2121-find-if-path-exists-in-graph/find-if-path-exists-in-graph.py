class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        for src, dst in edges : 
            adj[src].append(dst)
            adj[dst].append(src)

        q = deque([source])

        visit = set()
        while q : 
            node = q.popleft()

            if node in visit : 
                continue 


            visit.add(node)

            if node == destination : 
                return True 

            for nei in adj[node]: 
                q.append(nei)

        return False 