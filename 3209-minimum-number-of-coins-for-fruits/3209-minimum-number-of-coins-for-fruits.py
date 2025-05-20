class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        memo = {}  # Add memoization
                 
        def dfs(i): 
            if i > len(prices):
                return 0
                            
            if i in memo:  # Check memo
                return memo[i]
                
            #Take free options
            takeFreeFruits = float("inf")
                         
            # The key fix: After buying fruit at position i (1-indexed)
            # You can get fruits at positions i+1, i+2, ..., i+i for free
            # So the next purchase can be at position i+1, i+2, ..., i+i+1
            free_fruits_end = min(len(prices), i + i)
                         
            for t in range(i + 1, free_fruits_end + 2):
                takeFreeFruits = min(takeFreeFruits, prices[i - 1] + dfs(t))
             
            if takeFreeFruits == float("inf"):
                takeFreeFruits = prices[i - 1]
                          
            memo[i] = takeFreeFruits  # Store in memo
            return takeFreeFruits
         
        return dfs(1)