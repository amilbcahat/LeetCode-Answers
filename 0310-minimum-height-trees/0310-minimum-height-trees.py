class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #Intuition is to reach the middle , from there only we can minimize heights 
        #One of the craziest problems 
        #BFS from outside to inside !!!
        if n == 1: #or -> not edges condition
            return [0]

        adj = defaultdict(list)

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        leaves = deque()

        edge_cnt = {}
        
        for node in adj:
            nei = adj[node]
            if len(nei) == 1:
                leaves.append(node)
            edge_cnt[node] = len(nei)

        while leaves: 
            if n <= 2: 
                return list(leaves)

            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1 
                for nei in adj[node]:
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        leaves.append(nei)

        

            