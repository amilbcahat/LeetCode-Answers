class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        if len(nums) == 1: 
            #If length is 1, and curSum is equal to k, then we got one subarray, otherwise 0 
            return 1 if k == nums[-1] else 0

        total = 0 
        #Intuition
        #This map contains curSum to i info
        #Now the trick is , finding for prefix[i] - prefix[j] = k , this means there is a subarray that has sum equal to k , and that is between i and j 
        preMap = {0 : -1} #We got curSum of 0, even before Array had started, so count the length from beginning
        res = 0
        for r, num in enumerate(nums): 
            total += num 
            diff = total - k 
            if diff in preMap: 
                l = preMap[diff]
                res = max(res, r - l)
            if total not in preMap: 
                preMap[total] = r #For Maximum result , have it set on the first encounter
        return res