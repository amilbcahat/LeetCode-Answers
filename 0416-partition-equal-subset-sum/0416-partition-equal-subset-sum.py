class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False 

        dp = {}
        def dfs(i, curSum):
            nonlocal total
            if total // 2 == curSum:
                return True 

            if i >= len(nums):
                return False

            if (i, curSum) in dp:
                return dp[(i, curSum)]

            res = (dfs(i + 1, curSum + nums[i]) or dfs(i + 1, curSum))

            dp[(i, curSum)] = res
            return res 

        return dfs(0, 0)