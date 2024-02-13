class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #By logic of always choosing an element , just not the same one , twice 
        #Time and Memory Optimized Solution !
        res = []
        def dfs(i , curComb):
            if len(curComb) == k: 
                res.append(curComb.copy())
                return 
            
            if i > n : 
                return 

            for j in range(i , n + 1):
                curComb.append(j)
                dfs(j + 1 , curComb)
                curComb.pop()

        dfs(1 , [])
        return res
 
        #By Logic of Include or Not to Include - TC (O(n) * 2^n)
        # res = []
        # def dfs(i , curComb):
        #     if len(curComb) == k : 
        #         res.append(curComb.copy())
        #         return 

        #     if i > n : 
        #         return 

        #     #To include 
        #     curComb.append(i)
        #     dfs(i + 1, curComb)
        #     curComb.pop()

        #     #To not include
        #     dfs(i + 1 , curComb)

        # dfs(1, []) 
        # return res