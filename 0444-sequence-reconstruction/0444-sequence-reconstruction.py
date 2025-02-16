class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        if len(sequences) == 1 and (len(sequences[0]) == len(nums)): 
            return True 

        adj = defaultdict(list)
        indegree = defaultdict(int)
        nodes = set()
        for sequence in sequences: 
            for i in range(len(sequence) - 1):
                src = sequence[i]
                dst = sequence[i + 1]
                indegree[dst] += 1
                nodes.add(src)
                nodes.add(dst)
                adj[src].append(dst)

        queue = deque()
        for n in nodes: 
            if not indegree[n]: 
                queue.append(n)
        print(queue)
        level = 0 
        topSort = []
        while queue: 
            if len(queue) > 1 :  #Have one option only 
                return False
            node = queue.popleft()
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0: 
                    queue.append(nei)
            topSort.append(node)
            level += 1

        print(topSort)
        return level == len(nums) 

        # topSort = []
        # path = set()
        # visited = set()

        # print(adj, nodes)
        # def dfs(src): 
        #     if src in path: 
        #         return False

        #     if src in visited: 
        #         return True

        #     path.add(src)
        #     for nei in adj[src]: 
        #         if not dfs(nei):
        #             return False

        #     path.remove(src)
        #     visited.add(src)
        #     topSort.append(src)

        #     return True

        # for n in nodes: 
        #     if not dfs(n):
        #         return False
        # print(topSort[::-1])
        # return True
            