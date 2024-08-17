class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 , rob2 = 0 , 0 
        #[rob1 , rob2 , n , n + 1 , ...]

        for n in nums : 
            temp = max(rob1 + n , rob2)
            rob1 = rob2 
            rob2 = temp

        return rob2
        #Skip yourself and take rest of the array as subproblem
        #OR include yourself ,skip the next one and take the entire array as subproblem
        # dp = {}
        # def dfs(i) : 
        #     if i >= len(nums) :
        #         return 0 

        #     if i in dp : 
        #         return dp[i]

        #     res = max(dfs(i + 1) , nums[i] + dfs(i + 2))

        #     dp[i] = res
        #     return res 

        # return dfs(0)