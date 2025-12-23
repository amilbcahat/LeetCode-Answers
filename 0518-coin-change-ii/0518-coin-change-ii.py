class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i, a):
            if a == 0: 
                return 1

            if (i, a) in dp:
                return dp[(i, a)]
            
            if a < 0 or i >= len(coins):
                return 0

            res = 0 

            #pick
            res += dfs(i , a - coins[i])
            #not pick
            res += dfs(i + 1, a)

            dp[(i, a)] = res

            return res

        return dfs(0, amount)