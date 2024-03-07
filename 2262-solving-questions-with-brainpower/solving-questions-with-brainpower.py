class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        #Bottom-Up Approach
        dp = {}

        for i in range(len(questions) - 1 , -1 , -1):
            dp[i] = max(
                questions[i][0] + dp.get(i + 1 + questions[i][1] , 0),
                dp.get(i + 1 , 0)
            )

        return dp[0]

        #Top Down Approach
        # cache = {}
        # def dfs(i):
        #     if i >= len(questions):
        #         return 0 

        #     if i in cache : 
        #         return cache[i]

        #     #Take Question#
            
        #     take = questions[i][0] + dfs(i + (questions[i][1] + 1))

        #     #Dont take Question 
        #     skip = dfs(i + 1)

        #     cache[i] = max(take , skip)

        #     return cache[i]

        # return dfs(0)