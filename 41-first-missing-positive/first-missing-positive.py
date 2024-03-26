class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] == 0 : 
                nums[i] = len(nums) + 1 

        for n in nums :
            n = abs(n)

            if n > len(nums):
                continue 

            if nums[n - 1] < 0 : 
                continue 

            nums[n - 1] = -nums[n - 1]

        
        for i , n in enumerate(nums):
            if n > 0 : 
                return i + 1

        return len(nums) + 1
                