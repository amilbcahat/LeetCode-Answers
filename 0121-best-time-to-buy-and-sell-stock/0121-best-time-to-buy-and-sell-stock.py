class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        buyPrice = float("inf")
        r = -1
        l = -1
        profit = 0
        N = len(nums)
        for i, n in enumerate(nums): 
            if buyPrice > n: 
                buyPrice = n 
                r = N - i - 1
            
            if profit < n - buyPrice:
                profit = n -  buyPrice
                l = N - i - 1
        return profit