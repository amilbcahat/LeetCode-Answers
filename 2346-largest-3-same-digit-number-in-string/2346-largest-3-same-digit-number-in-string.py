class Solution:
    def largestGoodInteger(self, nums: str) -> str:
        
        res = float('-inf')

        for i in range(1 , len(nums) - 1):
            if nums[i - 1] == nums[i] == nums[i + 1]:
                res = max(res , int(nums[i]))

        return str(res) * 3 if res != float('-inf') else ""