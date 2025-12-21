class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = defaultdict(list)
        indegree = defaultdict(int)
        for i in range(len(recipes)):
            for ind in ingredients[i]:
                dst = recipes[i]
                src = ind
                adj[src].append(dst)
                indegree[dst] += 1


        queue = deque()
        lookup = set(recipes)
        res = set()
        for s in supplies:
            queue.append(s)

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                for nei in adj[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        if nei in lookup:
                            res.add(nei)
                        queue.append(nei)

        return list(res)