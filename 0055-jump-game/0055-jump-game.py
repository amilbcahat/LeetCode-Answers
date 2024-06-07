class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #Greedy 
        #Start from last position , shift the goal position , and see with each iteration if its reachable
        goal = len(nums) - 1

        for i in range(len(nums) - 1 , -1 , -1):
            #i + nums[i] is farthest jump distance 
            if i + nums[i] >= goal : 
                goal = i 

        return True if goal == 0 else False 


        #DP
        # dp = [False] * (len(nums))

        # dp[-1] = True 

        # for i in range(len(nums) - 2 , -1 , -1):
        #     furthestJump = min(i + nums[i] , len(nums) - 1)
        #     #Can make these length jumps 
        #     for j in range(i + 1 , furthestJump + 1):
        #         if dp[j] : 
        #             dp[i] = dp[j] #Can also write dp[i] = True 
        #             break

        # return dp[0]