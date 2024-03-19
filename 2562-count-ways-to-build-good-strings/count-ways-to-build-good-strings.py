class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        #Dynamic PRogramming method (less intuitive)-
        dp = {0 : 1} # length -> num of strs 
        mod = 10 ** 9 + 7 

        for i in range(1 , high + 1):
            dp[i] = (dp.get(i - one , 0) + dp.get(i - zero , 0)) % mod 

        
        #counts for all string of length between that range 
        return sum([dp[i] for i in range(low , high + 1)]) % mod 


        # res = 0
        # mod = 10 ** 9 + 7 
        # cache = {}
        # #This time a little different 
        # def dfs(resLen):
        #     nonlocal res
        #     if high < resLen :
        #         return 0

        #     if resLen in cache : 
        #         return cache[resLen]
            
        #     res = 1 if resLen >= low else 0 

        #     res += (dfs(resLen + zero)+ dfs(resLen + one))

        #     cache[resLen] = res % mod 
            
        #     return cache[resLen]  

            
        
        # return dfs(0)
