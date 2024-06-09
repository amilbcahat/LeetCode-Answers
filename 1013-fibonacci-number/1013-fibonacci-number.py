class Solution:
    def fib(self, n: int) -> int:
        #Constant space 
        p1 = 1 
        p2 = 0 

        tmp = 0 
        for i in range(n):
            tmp = p1 + p2 
            p1 = p2 
            p2 = tmp

        return tmp

        
        # dp = {}
        # def dfs(n) : 
        #     if n in dp : 
        #         return dp[n]
            
        #     if n == 0 : 
        #         return 0 

        #     if n == 1: 
        #         return 1

        #     dp[n] = dfs(n - 1) + dfs(n - 2) 

        #     return dp[n]

        # return dfs(n)