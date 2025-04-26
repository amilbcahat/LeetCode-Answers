class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        lastMinK = -1 
        lastMaxK = - 1
        leftBound = -1
        res = 0 

        for i in range(len(nums)): 
            if nums[i] > maxK or nums[i] < minK: 
                #We can take this into our consideration 
                #But from here we should calculate the combination of answers 
                leftBound = i 

            if nums[i] == maxK: 
                lastMaxK = i 
            
            if nums[i] == minK:
                lastMinK = i 

            startOfSubarray = min(lastMinK, lastMaxK)
            temp = startOfSubarray - leftBound #Calculates combination wise 

            res += temp if temp > 0 else 0 # leftBound will always be on left side of the minK, maxK

        return res