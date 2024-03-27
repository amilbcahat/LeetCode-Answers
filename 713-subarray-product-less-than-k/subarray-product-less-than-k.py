class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0 
        res = 0 
        curProd = 1 #Try to use more of your brain , dont reach the discussion tab much 
        for r in range(len(nums)):
            curProd *= nums[r]
            while l <= r and curProd >= k : 
                curProd = curProd // nums[l]
                l += 1 
                
            res += (r - l + 1) #Gives the no. of subarrays 

        return res 
            