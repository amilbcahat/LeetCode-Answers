class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()

        #Problem 1827 
        ans =  0 
        for i in range(1, len(nums)): 
            if nums[i - 1] >= nums[i]: 
                diff = (nums[i - 1] - nums[i] + 1)
                nums[i] += diff
                ans += diff

        return ans