class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False 

        dp = {}

        #BitSet DP
        targetBit = 1 << (total // 2)
        mask = targetBit - 1
        b = 1
        for num in nums: 
            b |= b << num

            if b & targetBit: 
                return True 
            
            b &= mask
        return False

        
        # def dfs(i, curSum):
        #     nonlocal total
        #     if total // 2 == curSum:
        #         return True 

        #     if i >= len(nums):
        #         return False

        #     if (i, curSum) in dp:
        #         return dp[(i, curSum)]

        #     res = (dfs(i + 1, curSum + nums[i]) or dfs(i + 1, curSum))

        #     dp[(i, curSum)] = res
        #     return res 

        return dfs(0, 0)