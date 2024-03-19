class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        #One thing is to note that , before it was 2^n backtracking soln , but with dp , we get linear time soln (we dont need to change and 
        #backtrack on basis of string , so two string can have same length but still different solution , still , we just need 
        # length of string , so its like , ek teer do nishaane !!)

        #Dynamic PRogramming method (less intuitive)-
        dp = {0 : 1} # length -> num of strs , just a normal base case !
        mod = 10 ** 9 + 7 
        #There is no need of low <= x <= high , check , since , 1 - D array has length of max high and starts from low , so its kind of obvious 
        #That string is built from 

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
