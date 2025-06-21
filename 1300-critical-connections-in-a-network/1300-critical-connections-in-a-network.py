class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.adj = defaultdict(list)
        nodes = set()
        art_con = []
        discovery = [-1] * n 
        low = [-1] * n 
         
        for src, dst in connections:
            self.adj[src].append(dst)
            self.adj[dst].append(src)
            nodes.add(src)
            nodes.add(dst)

        for node in nodes: 
            if discovery[node] == -1: 
                self.dfs(node, 1, -1, art_con, low, discovery)

        return art_con


    def dfs(self, curNode, time, parent, art_con, low, discovery):
        low[curNode] = discovery[curNode] = time
        for neighbor in self.adj[curNode]: 
            if parent == neighbor: 
                    continue 
                    
            if discovery[neighbor] == -1: 
                self.dfs(neighbor, time + 1, curNode, art_con, low, discovery)

                low[curNode] = min(low[curNode], low[neighbor])

                if low[neighbor] > discovery[curNode]: 
                    art_con.append([curNode, neighbor])

            else:
                low[curNode] = min(low[curNode], discovery[neighbor])


                    

        

        


            