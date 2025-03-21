class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = defaultdict(list)
        indegree = defaultdict(int)

        for i in range(len(recipes)): 
            for ind in ingredients[i]: 
                src = recipes[i]
                pre = ind 
                adj[ind].append(src)
                indegree[src] += 1

        queue = deque()
        lookup = set(recipes)
        res = set()
        for s in supplies:
            queue.append(s)

        while queue: 
            node = queue.popleft()
            for nei in adj[node]: 
                indegree[nei] -= 1
                if indegree[nei] == 0: 
                    if nei in lookup:
                        res.add(nei)
                    queue.append(nei)

        return list(res)
