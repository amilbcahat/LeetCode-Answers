




class Solution:
    def numSquares(self, n: int) -> int:
        #Same logic as Coin change problem ! just evaluate the coins here !
        dp = [float("inf")] * (n + 1)
        #To get zero coins , we need 0 coins 
        dp[0] = 0 
        #Another extra test case , since we can get 1 (perfect sum) to get 1 amounted sum 
        dp[1] = 1
        coins = [i ** 2 for i in range(1, n) if i ** 2 <= n]

        for a in range(1 , n+1):
            for c in coins : 
                if a - c >= 0 : 
                    dp[a] = min(dp[a] , 1 + dp[a - c]) 
        
        return dp[n] if dp[n] != float('inf') else -1  
