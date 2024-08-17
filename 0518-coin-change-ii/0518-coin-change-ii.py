class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i , a) : 
            if a > amount or i >= len(coins) : 
                return 0 

            if amount == a : 
                return 1 

            if (i , a) in dp : 
                return dp[(i , a)]

            res = 0
            res += (dfs(i , a + coins[i]) + dfs(i + 1 , a))

            dp[(i , a)] = res
            return res 

        return dfs(0 , 0)
