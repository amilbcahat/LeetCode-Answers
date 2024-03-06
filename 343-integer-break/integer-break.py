class Solution:
    def integerBreak(self, n: int) -> int:
        #Bottom up solution 
        dp = { 1 : 1}
        for num in range(2 , n + 1):
            dp[num] = 0 if num == n else num #Only n gets broken down , others can or cannot get broken down
            for i in range(1 , num):
                #Trying breaking down like we did recursively 
                val = dp[i] * dp[num - i]
                dp[num] = max(dp[num] , val)
                #
        return dp[n]

        # dp = { 1:  1}

        # #Logic is to break every coin 
        # def dfs(num):
        #     if n == 1 : 
        #         return 1 

        #     if num in dp : 
        #         return dp[num]

        #     #
        #     #Making sure that original coin is broken down , but not the subsequent subproblems
        #     #initializing with zero ensures the breakdown 
        #     dp[num] = 0 if num == n else num 
        #     for i in range(1 , num):
        #         val = dfs(i) * dfs(num - i)
        #         dp[num] = max(dp[num] , val)

        #     return dp[num]

        # return dfs(n)