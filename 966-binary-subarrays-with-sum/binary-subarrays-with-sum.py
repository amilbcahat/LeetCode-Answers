class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        #Subarray with K Sum logic !
        res = 0 
        curSum = 0 
        prefixSum = {0 : 1}

        for n in nums : 
            curSum += n 
            diff = curSum - goal 
            res += prefixSum.get(diff , 0)
            prefixSum[curSum] = 1 + prefixSum.get(curSum ,0)

        return res 