class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #Same Logic as before 
        #Res has last value !
        # ans = len(nums) 
        # for i in range(len(nums)):
        #     #Each XOR 
        #     x = i^nums[i]
        #     #Storing the missing number here 
        #     ans = ans^x
        
        #Cyclic Sort (More Intuitive Pattern for this) 
        i = 0 
        while (i < len(nums)):
            correctIndx = nums[i]
            if nums[i] < len(nums) and nums[i] != nums[correctIndx]:
                nums[i], nums[correctIndx] = nums[correctIndx], nums[i]
            else: 
                i+= 1 

        for i in range(len(nums)):
            if nums[i] != i : 
                return i 
        
        return len(nums)