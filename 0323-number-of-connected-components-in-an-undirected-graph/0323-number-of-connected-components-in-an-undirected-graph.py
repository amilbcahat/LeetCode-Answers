class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for src, dst in edges: 
            adj[src].append(dst)
            adj[dst].append(src)


        visit = set()

        def dfs(node):
            visit.add(node)
            # comp_map[node] = comp_no

            for nei in adj[node]:
                if nei not in visit:
                    dfs(nei)


        comp_no = 0
        for i in range(n):
            if i not in visit: 
                comp_no += 1
                dfs(i)

        return comp_no
                