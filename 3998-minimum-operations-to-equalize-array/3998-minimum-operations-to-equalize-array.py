class Solution:
    def minOperations(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                return 1 
        
        return 0