class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost) - 3 , -1  ,-1) : 
            cost[i] += min(cost[i + 1] , cost[i + 2])

        return min(cost[0] , cost[1])

        # dp = {}
        # def dfs(i) : 
        #     if i >= len(cost): 
        #         return 0 

        #     if i in dp : 
        #         return dp[i]

        #     res = min(cost[i] + dfs(i + 1), cost[i] + dfs(i + 2))

        #     dp[i] = res

        #     return res 

        # return min(dfs(0) , dfs(1))