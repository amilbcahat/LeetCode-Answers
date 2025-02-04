class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #Cycle Sort 
        i = 0 
        while  i < len(nums): 
            correctIndx = nums[i] - 1
            if nums[i] != nums[correctIndx]: 
                nums[i], nums[correctIndx] = nums[correctIndx], nums[i]
            else: 
                i += 1 
        
        print(nums)
        res = []

        for i in range(len(nums)): 
            if nums[i] != i + 1:
                res.append(i + 1)
        
        return res