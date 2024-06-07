class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #DP
        dp = [False] * (len(nums))

        dp[-1] = True 

        for i in range(len(nums) - 2 , -1 , -1):
            furthestJump = min(i + nums[i] , len(nums) - 1)
            #Can make these length jumps 
            for j in range(i + 1 , furthestJump + 1):
                if dp[j] : 
                    dp[i] = dp[j] 
                    break

        return dp[0]