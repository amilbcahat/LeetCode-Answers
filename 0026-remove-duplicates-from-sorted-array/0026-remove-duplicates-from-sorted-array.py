class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        #Neetcode solution 
        #First elment is a unique elem in itself ! 
        L = 1

        for R in range(1,len(nums)):
            #Unique elements found ! 
            if nums[R] != nums[R-1]:
                nums[L] = nums[R]
                L+=1
        return L


        

        #My solution ! 
        # k = 0 
        # curElem = float("-inf")
        # for i in range(len(nums)):
        #     if curElem != nums[i]:
        #         curElem = nums[i]
        #         nums[k] = curElem
        #         k += 1 

        # return k