class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #Base Case Handling
        # if len(nums) == 1 : 
        #     if nums[0] == 1 : 
        #         return 2 
        #     else: 
        #         return 1

        # #Shifted Negs to Last
        # l , r = 0 , len(nums) - 1
        # while l < r : 
        #     while l < r and l < len(nums) - 1 and nums[l] > 0 : 
        #         l += 1 
            
        #     while l < r and r > 1 and  nums[r] <= 0: 
        #         r -= 1
            
        #     if l < r and nums[l] <= 0 and nums[r] > 0:
        #         nums[l], nums[r] = nums[r], nums[l]
            
        #     l += 1 
        #     r -= 1

        # ind = -1 
        # for i in range(len(nums)): 
        #     if nums[i] <= 0: 
        #         ind = i
        #         break

        # if ind == -1:
        #     #If all positive
        #     r = len(nums) - 1
        # else : 
        #     #pos - neg boundary
        #     r = ind - 1

        #Cylic sort to sort pos numbers, index based
        i = 0 
        while i < len(nums): 
            print(i)
            correctIndx = nums[i] - 1
            if nums[i] > 0 and nums[i] <= len(nums)  and nums[i] != nums[correctIndx]: 
                nums[i], nums[correctIndx] = nums[correctIndx], nums[i]
            else: 
                i += 1

        print(nums)
        
        #Then finding the missing number 
        for i in range(len(nums)): 
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1#+1 , to manage index and +1 to tell for the case where missing number is more than the length of pos number subarray