class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = float("inf")
        profit = 0 

        for price in prices : 
            if buyPrice > price : 
                buyPrice = price  
            
            #buy price should be minimum 
            profit = max(profit , price - buyPrice)

        return profit