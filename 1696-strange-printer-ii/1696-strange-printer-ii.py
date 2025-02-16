class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        #colors are real dependency here !!
        n = len(targetGrid)
        m = len(targetGrid[0])
        colors = set()
        squares = defaultdict(list) #color -> to square map
        for i in range(n):
            for j in range(m):
                color = targetGrid[i][j]
                colors.add(targetGrid[i][j])
                if color not in squares: 
                    squares[color] = [float("inf"), 0, float("inf"), 0]
                squares[color][0] = min(squares[color][0], i)
                squares[color][1] = max(squares[color][1], i)
                squares[color][2] = min(squares[color][2], j)
                squares[color][3] = max(squares[color][3], j)

        adj = defaultdict(list)
        indegree = defaultdict(int)
        queue = deque()

        for color in colors: 
            #Within this color , check for further dependencies 
            visited= set([color])
            for i in range(squares[color][0], squares[color][1] + 1):
                for j in range(squares[color][2], squares[color][3] + 1):
                    if targetGrid[i][j] not in visited: 
                        visited.add(targetGrid[i][j])
                        indegree[targetGrid[i][j]] += 1
                        adj[color].append(targetGrid[i][j])

        for color in colors: 
            if color not in indegree: 
                queue.append(color)

        res = 0 

        while queue: 
            color = queue.popleft()
            for adjColor in adj[color]: 
                indegree[adjColor] -= 1
                dependency = indegree[adjColor]
                if dependency == 0: 
                    queue.append(adjColor)
            res += 1

        return res == len(colors)

                