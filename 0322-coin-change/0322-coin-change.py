class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount+1)
        dp[0] = 0 
        #Bottom UP
        #a is amount 
        #dp[7] = 1 + dp[3]
        for a in range(1 , amount + 1) : 
            for c in coins : 
                if a - c >= 0 : 
                    dp[a] = min(dp[a] , 1 + dp[a - c])

        return dp[amount] if dp[amount] != float("inf") else -1
        # dp = {}

        # for i in coins : 
        #     dp[i] = 1

        # def getResult(amount):
        #     if amount == 0 : 
        #         return 0 

        #     if amount in dp : 
        #         return dp[amount]
            
        #     k = float("inf")
        #     for c in coins : 
        #         if amount - c >= 0 : 
        #             k = min(k , 1+getResult(amount-c))

        #     dp[amount] = k 
        #     return dp[amount]
        # print(dp)
        # return getResult(amount) if getResult(amount) != float("inf") else -1 