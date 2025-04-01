class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = {}
        def dfs(i): 
            if i >= len(questions): 
                return 0 
            
            if i in dp: 
                return dp[i]

            skip = dfs(i + 1)
            include = questions[i][0] + dfs(i + (questions[i][1] + 1))
            points = max(skip, include)

            dp[i] = points
            return points

        return dfs(0)
