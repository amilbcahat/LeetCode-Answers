class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        #Iterative 
        n = len(questions)
        cache = [0] * n 

        for i in reversed(range(n)): 
            points, brainp = questions[i]
            next_i = i + brainp + 1
            include = points + (cache[next_i] if next_i < n else 0)
            skip = cache[i + 1] if i + 1 < n else 0 
            cache[i] = max(skip, include)
        
        return cache[0]

        # Recursive 
        # dp = {}
        # def dfs(i): 
        #     if i >= len(questions): 
        #         return 0 
            
        #     if i in dp: 
        #         return dp[i]

        #     skip = dfs(i + 1)
        #     include = questions[i][0] + dfs(i + (questions[i][1] + 1))
        #     points = max(skip, include)

        #     dp[i] = points
        #     return points

        # return dfs(0)
