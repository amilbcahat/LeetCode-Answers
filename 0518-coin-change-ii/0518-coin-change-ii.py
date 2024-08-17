class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #Memory Optimal Pure DP (it follows the grid diagram here) :- 
        dp = [0] * (amount + 1)
        dp[0] = 1 

        for i in range(len(coins) - 1, -1 , -1) : 
            nextDp = [0] * (amount + 1)
            nextDp[0] = 1 
            #Skipping the current coin (just look one below , and see if they reach to that amount)
        #.  #Seeing below (as per diagram)
            for a in range(1 , amount + 1) : 
                nextDp[a] = dp[a]
                 #Taking the current coin into consideration (just look to right on index equal to a-coins[i])
        #         #Seeing on right side (as per diagram)
                if a - coins[i] >= 0 : 
                    nextDp[a] += nextDp[a - coins[i]]
            dp = nextDp 

        return dp[amount]

        # dp = [[0] * (len(coins)+1) for i in range(amount+1)]
        # dp[0] = [1] * (len(coins)+1)

        # #Code Grid -> 
        # # amount ->  5   4   3   2   1   0 
        # #            0   0   0   0   0   1  1             <- x amount can be made using 1,2,5 coins    
        # #            0   0   0   0   0   1  2   ^         <- x amount can be made using 2,5 coins
        # #            0   0   0   0   0   1  5   |         <- x amount can be made using 5 coin
        # #            0   0   0   0   0   1    coins 
        # # Last one is dummy row for skipping condition edge case and the matrix is initialized inverted this , representation is just to imitate knapsack pattern ! 
        # # Code implemented is inverting this 
        
        # for a in range(1 , amount + 1):
        #     for i in range(len(coins) - 1 , -1 , -1):
        #         #Skipping the current coin (just look one below , and see if they reach to that amount)
        #         #Seeing below (as per diagram)
        #         dp[a][i] = dp[a][i + 1]
        #         #Taking the current coin into consideration (just look to right on index equal to a-coins[i])
        #         #Seeing on right side (as per diagram)
        #         if a - coins[i] >= 0 : 
        #             dp[a][i] += dp[a - coins[i]][i]

        # return dp[amount][0]

        #Easiest and most elegant
        # dp = [0] * (amount + 1)
        # dp[0] = 1 #number of way to reach 0 denomination 

        # #Maintains order for not counting permutation of sum of coins and thats why outer loop has to be coins 
        # for c in coins : 
        #     for a in range(c , amount + 1): 
        #         dp[a] += dp[a - c]

        # return dp[amount]


        # dp = {}
        # def dfs(i , a) : 
        #     if a > amount or i >= len(coins) : 
        #         return 0 

        #     if amount == a : 
        #         return 1 

        #     if (i , a) in dp : 
        #         return dp[(i , a)]

        #     res = 0
        #     res += (dfs(i , a + coins[i]) + dfs(i + 1 , a))

        #     dp[(i , a)] = res
        #     return res 

        # return dfs(0 , 0)