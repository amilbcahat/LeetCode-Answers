class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 1 
        curCounter = 1 
        for R in range(1 , len(nums)):
            if nums[R] != nums[R - 1]:
                nums[L] = nums[R]
                L += 1 
                curCounter = 1 
            elif nums[R] == nums[R - 1] and curCounter < 2 :
                nums[L]  = nums[R]
                L += 1
                curCounter += 1 

        return L 