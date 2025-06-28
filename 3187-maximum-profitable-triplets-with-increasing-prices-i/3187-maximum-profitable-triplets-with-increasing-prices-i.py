class Solution:
    def getMaxProfit(self, bit, priceIndex):
        i = priceIndex 
        res = 0
        while i > 0: 
            res = max(bit[i], res)
            i -= i & -i
        return res

    def updateProfit(self, bit, priceIndex, profit):
        i = priceIndex 
        while i > 0 and i < len(bit): 
            bit[i] = max(bit[i], profit)
            i += i & -i

    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        n = len(prices)
        maxPrice = max(prices)
        bitMaxLeft = [0] * (maxPrice + 1)
        bitMaxRight = [0] * (maxPrice + 1)
        maxLeftProfit = [0] * n
        for i in range(n): 
            maxLeftProfit[i] = self.getMaxProfit(bitMaxLeft, prices[i] - 1)
            self.updateProfit(bitMaxLeft, prices[i], profits[i])

        maxTotalprofit = -1 

        for i in range(n - 1, -1 , -1):

            adjustedPrice = maxPrice - prices[i] + 1
            maxRightProfit = self.getMaxProfit(bitMaxRight, adjustedPrice - 1)

            if maxLeftProfit[i] > 0 and maxRightProfit > 0: 
                maxTotalprofit = max(maxTotalprofit, maxLeftProfit[i] + profits[i] + maxRightProfit)
            
            self.updateProfit(bitMaxRight, adjustedPrice, profits[i])

        return maxTotalprofit
