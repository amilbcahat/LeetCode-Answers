class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 
        curSum = 0 
        prefixSum = {0  :  1} # when 3 - 3 = 0 , in that case count for one possible subarray 

        for n in nums : 
            curSum += n 
            diff = curSum - k #part that if chopped off (calculated from start) , sums up to k 
            res += prefixSum.get(diff , 0) #If that prefix chop can happen and is available , then it would be added to result
            prefixSum[curSum] = 1 + prefixSum.get(curSum , 0)

        return res 