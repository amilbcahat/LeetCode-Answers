class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        # cacheTwo = {}
        # def pow(x, n): 
        #     if n == 0: 
        #         return 1 
            
        #     if (x, n) in cacheTwo:
        #         return cacheTwo[(x, n)]

        #     res = pow(x, n // 2)
        #     ans = -1
        #     if n & 1: 
        #         ans = x * res * res
        #     else: 
        #         ans = res * res
        #     cacheTwo[(x, n)] = ans
        #     return ans

        # MOD = 10 ** 9 + 7 
        # dp = [[0] * (n + 1) for _ in range(n + 1)]
        # dp[0][0] = 1

        # for i in range(1, n + 1): 
        #     val = i ** x 
        #     for j in range(n + 1): 
        #         dp[i][j] = dp[i - 1][j]
        #         if j >= val: 
        #             dp[i][j] = (dp[i][j] + dp[i - 1][j - val]) % MOD

        # return dp[n][n]
        #Space optimized 

        MOD = 10 ** 9 + 7 
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1): 
            val = i ** x
            if val > n: 
                break 
            for j in range(n, val - 1, -1):
                dp[j] = (dp[j] + dp[j - val]) % MOD 

        return dp[n]

