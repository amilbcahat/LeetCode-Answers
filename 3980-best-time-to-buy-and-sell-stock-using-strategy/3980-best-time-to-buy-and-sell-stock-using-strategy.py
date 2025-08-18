class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        # Explanation - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/solutions/7090859/beats-100-simple-for-loop-easy-code-detailed-explanation-with-visual-diagram/
        n = len(prices)
        h = k // 2

        sp = [st * pr for st, pr in zip(strategy, prices)]
        base = sum(sp)

        if n == k: 
            change = sum(prices[h:]) - base
            return base + max(0, change)

        win_orig = sum(sp[:k])
        win_new = sum(prices[h :k])
        max_ch = win_new - win_orig

        for i in range(1, n - k + 1): 
            win_orig += (sp[i + k - 1] - sp[i - 1])
            win_new += (prices[i + k - 1] - prices[i + h - 1])
            max_ch = max(max_ch, win_new - win_orig)
        
        return base + max(0, max_ch)