class Solution:
    def jump(self, nums: List[int]) -> int:
         #Use BFS intuition here we take each jump as a layer !
        # l , r define the limits of the current layer
        # l = r + 1 takes r to the next level and r to the farther reachable position 
     
        res = 0 
        l , r = 0 , 0 

        while r < len(nums) - 1 : 
            farthest = 0 

            for i in range(l , r + 1 ):
                farthest = max(farthest , i + nums[i])

            #Next layer min index 
            l = r + 1 
            #Next layer max index , basically window of next layer , since it is farthest , it will eventually reach the last index
            r = farthest 
            res += 1 
        return res 


        #Top - Down Approach 
        # dp = {}
        # def dfs(i):

        #     if i in dp : 
        #         return dp[i]

        #     if i == len(nums) - 1:
        #         return 0

        #     if i >= len(nums):
        #         return float("inf")


        #     jumpRange = i + nums[i]
        #     res = float("inf")
        #     for t in range(i + 1 , jumpRange + 1):
        #         res =  min(res , 1 + dfs(t))

        #     dp[i] = res 
        #     return res 

        # return dfs(0)

        #Tabular Method
        
        # dp = [0] * len(nums)

        # dp[-1] = 1

        # for i in range(len(nums) - 2, -1 , -1):
        #     furthestJump = min(i + nums[i], len(nums) - 1)
        #     res = float("inf")
        #     for j in range(i + 1, furthestJump + 1):
        #         res = min(res , 1 + dp[j])

        #     dp[i] = res
                
        # return dp[0] - 1

