class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        #Marking 0 and neg elements with len of more than the arrat 
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] == 0 : 
                nums[i] = len(nums) + 1

        
        for n in nums : 
            n = abs(n)
            #Dont consider length of more than the array (they cant be mapped)
            if n > len(nums): 
                continue
            
            
            if nums[n - 1] < 0 : 
                #Already visited then move on and ignore
                continue 

            #Mark as visited , if can be mapped with the array 
            nums[n - 1] = -1 * nums[n - 1] 

        
        for i , n  in enumerate(nums):
            if n > 0 : 
                #Not visited 
                return i + 1

        print(nums)
        return len(nums) + 1 #Does not have a missing integer in the indexes of the array , so first missing integer must come after the array , which would be the len(nums) + 1 itself