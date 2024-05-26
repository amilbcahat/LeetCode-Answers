class Solution:
    def checkRecord(self, n: int) -> int:

        MOD = 10 ** 9 + 7 
        dp = [[[-1] * 3 for _ in range(2)] for _ in range(n + 1)]

        def dfs(i , A , L): 
            if A >= 2 or L >= 3 : 
                return 0 
####
            if i == 0 :
                return 1 

            if dp[i][A][L] != -1 : 
                return dp[i][A][L]

            ans = dfs(i - 1 , A , 0) #Present 
            ans += dfs(i - 1 , A , L + 1) #Late
            ans += dfs(i - 1 , A + 1 , 0) # Absent 

            dp[i][A][L] = ans % MOD 
            return dp[i][A][L]

        return dfs(n , 0 ,0 )

        # MOD = 10**9 + 7 

        # cache = {}
        # def count(n): 
        #     if n == 1 : 
        #         #A , L (consecutive)
        #         return {
        #             (0, 0) : 1 , (0, 1): 1 , (0, 2) : 0 , 
        #             (1, 0) : 1 , (1, 1): 0 , (1, 2) : 0  
        #         } #

        #     if n in cache : 
        #         return cache[n]

        #     tmp = count(n - 1)
        #     res = defaultdict(int)

        #         #Choose P 
        #     res[(0 , 0)] = ((tmp[(0, 0)] + tmp[(0, 1)]) % MOD + tmp[(0, 2)]) % MOD 
        #     res[(1 , 0)] = ((tmp[(1, 0)] + tmp[(1, 1)]) % MOD + tmp[(1, 2)]) % MOD 

        #         #Choose L
        #     res[(0, 1)] = tmp[(0 , 1)]
        #     res[(1, 1)] = tmp[(1 , 0)]
        #     res[(0, 2)] = tmp[(0 , 1)]
        #     res[(1, 2)] = tmp[(1 , 1)]

        #         #Choose A
        #         #ignore sec row , because a needs to be fewer than 2 
        #     res[(1, 0)] = (res[(1,0)] + (((tmp[(0, 0)] + tmp[(0, 1)]) % MOD + tmp[(0, 2)])) % MOD) % MOD

        #     cache[n] = res 
        #     return res 

        # return sum(count(n).values()) % MOD 
