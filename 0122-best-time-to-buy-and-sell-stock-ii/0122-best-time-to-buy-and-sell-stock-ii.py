class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Buy and sell at all points possible whenever saw a decline 
        profit = 0 

        for i in range(1 , len(prices)):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])

        return profit 

        #NeetCode Buy and Sell Template 
        
        # dp = {}

        # def dfs(i,buying):
        #     if i >= len(prices):
        #         return 0 

        #     if (i,buying) in dp : 
        #         return dp[(i,buying)]
        
        #     if buying : 
        #         buy = dfs(i+1, not buying) - prices[i]
        #         skip = dfs(i+1, buying)
        #         dp[(i,buying)] = max(buy , skip)
        #     else : 
        #         #Here buying was false initially indicating we cant buy 
        #         #But we will change that to not buying , which will make value True , meaning we can buy after selling !
        #         sell = dfs(i+1, not buying) + prices[i]
        #         skip = dfs(i+1, buying)
        #         dp[(i,buying)] = max(sell,skip)
        #     return dp[(i,buying)]

        # return dfs(0,True)