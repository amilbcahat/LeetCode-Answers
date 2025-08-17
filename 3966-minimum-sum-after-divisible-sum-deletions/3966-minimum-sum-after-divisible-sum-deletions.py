class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        #Solution here - https://leetcode.com/problems/minimum-sum-after-divisible-sum-deletions/
        total = sum(nums)
        preMap = defaultdict(lambda: float('-inf'))
        preMap[0] = 0  # remainder 0 -> dp[0] - prefix[0] = 0 - 0 = 0
        n = len(nums)
        dp = [0] * (n + 1)
        prefix = 0
        
        # dp[i] means max sum that can be removed using first i elements
        for i in range(1, n + 1):  # Fixed: n+1 to process all elements
            prefix += nums[i - 1]  # nums[i-1] because dp is 1-indexed
            remainder = prefix % k
            
            # Option 1: Skip current element
            dp[i] = dp[i - 1]
            
            # Option 2: Remove subarray ending at current position
            if remainder in preMap and preMap[remainder] != float('-inf'):
                candidate = preMap[remainder] + prefix
                dp[i] = max(dp[i], candidate)
            
            # Update preMap: store max(dp[j] - prefix[j]) for this remainder
            val = dp[i] - prefix
            preMap[remainder] = max(preMap[remainder], val)
        
        return total - dp[n]