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
            
            if low <= resLen <= high: 
                #One Good String found !
                res = 1 
            else : 
                res = 0 

            res += (dfs(resLen + zero)%mod + dfs(resLen + one)%mod)

            cache[resLen] = res % mod 
            
            return cache[resLen]  

            
        
        return dfs(0)
