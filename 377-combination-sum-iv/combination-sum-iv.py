class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #Bottom - up Approach !
        dp = [0] * (target + 1)
        #To reach 0 target , we can do it in one way ! (this was diff in coin change problem , where we had to take dp[0] = 0, because , to reach 0 , we
        #We did not require any coins)
        dp[0] = 1
        for i in range(target + 1):
            for n in nums : 
                if i - n >= 0 :
                    #We add all the subproblem ways  
                    #Unlike coin change problem , where , we just had to take min , number of coins 
                    dp[i] = dp[i] + dp[i - n]

        print(dp)
        return dp[-1]


        #Top - Down Approach !
        # #Test with res list , thats why added comments 
        # cache = {}
        # def dfs(totalSum 
        # # , res
        # ): 
        #     if totalSum == 0 : 
        #         # print(res)
        #         return 1 

        #     if totalSum in cache : 
        #         return cache[totalSum]

        #     if totalSum < 0 : 
        #         return 0 

        #     res = 0 
        #     for n in nums : 
        #         # res.append(n)
        #         res += dfs(totalSum - n 
        #         # , res
        #         )
        #         # res.pop(-1)

        #     cache[totalSum] = res 
            
        #     return res 

        # return dfs(target
        # # , []
        # )

