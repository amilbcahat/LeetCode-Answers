class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {}
        
        def dfs(n) : 
            if n == 0 : 
                return 0 

            if n == 1 : 
                return 1 

            if n == 2 : 
                return 1 

            if n in cache : 
                return cache[n]

            cache[n] = dfs(n - 1) + dfs(n - 2) + dfs(n - 3)

            return cache[n]

        return dfs(n)