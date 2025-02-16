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

        edge_cnt = {}
        leaves = deque()
        for src, neighbours in adj.items():
            if len(neighbours) == 1: 
                leaves.append(src)
            edge_cnt[src] = len(neighbours)

        while leaves: 
            if n <= 2: #Intuition , that , when reducing the leaves, if less/equal than 2 left then thats leaf nodes !!
                return list(leaves)

            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in adj[node]:
                    edge_cnt[nei] -= 1 
                    if edge_cnt[nei] == 1: #condition for leaf node  
                        #Is a leaf node 
                        leaves.append(nei)