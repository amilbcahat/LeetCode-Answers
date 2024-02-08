class Solution:
    def numSquares(self, n: int) -> int:
        #Same logic as Coin change problem ! just evaluate the coins here !
        dp = [float("inf")] * (n + 1)
        #To get zero coins , we need 0 coins 
        dp[0] = 0 
        #Another extra test case , since we can get 1 (perfect sum) to get 1 amounted sum 
        dp[1] = 1

        #Little bit enchanced method !
        for a in range(1 , n+1):
            c = 1 
            while c * c <= a : 
                #We look for squares till that amount 
                dp[a] = min(dp[a] , 1 + dp[a - (c * c)]) 
                c += 1    
        return dp[n] if dp[n] != float('inf') else -1  
