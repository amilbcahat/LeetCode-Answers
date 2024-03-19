class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        res = 0
        mod = 10 ** 9 + 7 
        cache = {}
        #This time a little different 
        def dfs(resLen):
            nonlocal res
            if high < resLen :
                return 0

            if resLen in cache : 
                return cache[resLen]
            
            res = 1 if resLen >= low else 0 

            res += (dfs(resLen + zero)+ dfs(resLen + one))

            cache[resLen] = res % mod 
            
            return cache[resLen]  

            
        
        return dfs(0)
