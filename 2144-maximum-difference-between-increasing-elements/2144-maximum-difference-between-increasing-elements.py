class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        buyPrice = float("inf")
        profit = 0
        for price in nums: 
            if buyPrice > price:
                buyPrice = price

            profit = max(profit, price - buyPrice)
        return profit if profit else -1