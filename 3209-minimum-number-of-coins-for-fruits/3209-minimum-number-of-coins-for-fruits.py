class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
            
        @cache
        def dfs(i): 
            if i >= len(prices): 
                return 0

            ans = float("inf")
            for next_pur in range(i + 2): 
                ans = min(ans, prices[i] + dfs(i + next_pur + 1))

            return ans

        return dfs(0)