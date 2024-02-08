
# Given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

# Example 1:

# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
 
#Solution 1 => n * sqrt(n)
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

#Solution 2 ->  n * sqrt(n)
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

#Solution 3 -> Lagrange 3 and 4 Theorem 