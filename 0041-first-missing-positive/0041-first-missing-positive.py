class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #Cylic sort to sort pos numbers, index based
        i = 0 
        while i < len(nums): 
            print(i)
            correctIndx = nums[i] - 1
            if nums[i] > 0 and nums[i] <= len(nums)  and nums[i] != nums[correctIndx]: 
                nums[i], nums[correctIndx] = nums[correctIndx], nums[i]
            else: 
                i += 1
        
        #Then finding the missing number 
        for i in range(len(nums)): 
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1