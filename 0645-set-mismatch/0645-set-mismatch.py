class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        #Cyclic Sort 
        #Cyclic Sort 
        i = 0 
        n = len(nums)
        while i < n : 
            correctIndx = nums[i] - 1
            if nums[i] != nums[correctIndx]: 
                nums[i], nums[correctIndx] = nums[correctIndx], nums[i]
            else: 
                i += 1 
        
        for i in range(len(nums)): 
            if nums[i] != i + 1: 
                return [ nums[i], i + 1]