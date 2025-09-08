class Solution:
    def minOperations(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            #if there is a change then bro, convert all
            if nums[i] != nums[i + 1]:
                return 1 
        #otherwise not needed 
        return 0