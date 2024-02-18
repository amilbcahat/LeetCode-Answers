class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        #Bottom up Approach -> 
        two = nums[-1] == nums[-2]
        if len(nums) == 2: 
            return two 

        three = (nums[-1] == nums[-2] == nums[-3] or nums[-3] + 1 == nums[-2] == nums[-1] - 1)
        ##Element gets shifted ! , Using the logic by declaring base cases and check each index of dp aray (not memory optimized) , shows T meaning , that condition is valid there 
        #Here , we needed only past three values , so we declared dp array like this !
        # because we need to check Truth value of i + 3 or i + 2 value
        dp = [three , two , False]
        for i in range(len(nums) - 4 , -1 , -1):
            cur = nums[i] == nums[i + 1] and dp[1]
            cur = cur or (
                (nums[i] == nums[i + 1] == nums[i + 2] or 
            nums[i] + 1 == nums[i + 1] == nums[i + 2] - 1) and 
            dp[2]
            )
            dp = [cur , dp[0] , dp[1]]
        return dp[0]
#
# DP Top Down Approach -> 
#         dp = {}
#         def dfs(i):
#             if i == len(nums):
#                 #When reached length , that means we can equally parition them 
#                 return True 
# #
#             if i in dp : 
#                 return dp[i]

#             res = False 
#             if i < len(nums) - 1 and nums[i] == nums[i + 1]:
#                 #Increment twice if this partition is possible 
#                 res = dfs(i + 2)
#             if i < len(nums) - 2 :
#                 if (nums[i] == nums[i + 1] == nums[i + 2] or nums[i] + 1 == nums[i + 1] == nums[i + 2] - 1):
#                 #Increment thrice if this partition is possible #
#                     res = res or dfs(i + 3)

#             dp[i] = res 

#             return res 

#         return dfs(0)
