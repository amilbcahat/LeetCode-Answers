class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        
        dp = {}
        def dfs(i):
            if i == len(nums):
                #When reached length , that means we can equally parition them 
                return True 
#
            if i in dp : 
                return dp[i]

            res = False 
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                #Increment twice if this partition is possible 
                res = dfs(i + 2)
            if i < len(nums) - 2 :
                if (nums[i] == nums[i + 1] == nums[i + 2] or nums[i] + 1 == nums[i + 1] == nums[i + 2] - 1):
                #Increment thrice if this partition is possible #
                    res = res or dfs(i + 3)

            dp[i] = res 

            return res 

        return dfs(0)
