class Solution:
    def maxProfit(self, prices, profits):
        # Find the maximum price from the prices array
        maxPrice = 0
        n = len(prices)
        for price in prices:
            maxPrice = max(maxPrice, price)

        # Initialize Binary Indexed Trees (BIT) for left and right max profits
        bitForMaxLeft = [0] * (maxPrice + 1)
        bitForMaxRight = [0] * (maxPrice + 1)

        # Array to store max profit for the left side of each price
        maxLeftProfit = [0] * n

        # Calculate maxLeftProfit using BIT for each price
        for i in range(n):
            maxLeftProfit[i] = self.getMaxProfit(bitForMaxLeft, prices[i] - 1)
            self.updateBIT(bitForMaxLeft, prices[i], profits[i])

        # Initialize the result as -1 indicating no valid triplet found yet
        maxTotalProfit = -1

        # Traverse the prices array from right to left to calculate the result
        for i in range(n - 1, -1, -1):
            adjustedPrice = maxPrice - prices[i] + 1
            maxRightProfit = self.getMaxProfit(bitForMaxRight, adjustedPrice - 1)

            # Update maxTotalProfit if both maxLeftProfit and maxRightProfit are greater than 0
            if maxLeftProfit[i] > 0 and maxRightProfit > 0:
                maxTotalProfit = max(maxTotalProfit, maxLeftProfit[i] + profits[i] + maxRightProfit)
            self.updateBIT(bitForMaxRight, adjustedPrice, profits[i])

        return maxTotalProfit

    # Update BIT with the new profit value at the given price index
    def updateBIT(self, bit, priceIndex, profit):
        i = priceIndex
        while i > 0 and i < len(bit):
            bit[i] = max(bit[i], profit)
            i += i & -i

    # Get the maximum profit value from BIT for a given price index
    def getMaxProfit(self, bit, priceIndex):
        maxProfit = 0
        i = priceIndex
        while i > 0:
            maxProfit = max(bit[i], maxProfit)
            i -= i & -i
        return maxProfit