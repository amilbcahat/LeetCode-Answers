class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #State : Buying or Selling ? 
        # If Buy -> i+1
        # If Sell -> i+2 (+1 for necessary cooldown)
        dp = {} #key = (i , buying) val = max_profit 

        def dfs(i , buying):
            #Empty Array Condition 
            if i>=len(prices):
                return 0 
            
            if (i , buying) in dp: 
                return dp[(i , buying)]

            if buying:
                #Next buy will be False 
                buy = dfs(i+1, not buying) - prices[i]
                cooldown = dfs(i+1 , buying)
                dp[(i,buying)] = max(buy , cooldown)
            else : 
                #Next buy will be True 
                sell = dfs(i+2, not buying) + prices[i]
                cooldown = dfs(i+1 , buying)
                dp[(i,buying)] = max(sell , cooldown)
            
            return dp[(i, buying)]

        return dfs(0 , True)