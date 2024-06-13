class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        lastMinK = -1
        lastMaxK = -1
        res = 0 
        culpritIndex = -1
        # https://leetcode.com/problems/count-subarrays-with-fixed-bounds/solutions/4949239/counting-fixed-bound-subarrays-with-two-pointers/
        for i in range(len(nums)):
            if nums[i] > maxK or nums[i] < minK :
                #Where existing subarray ends 
                culpritIndex = i

            if nums[i] == maxK :
                lastMaxK = i
            
            if nums[i] == minK :
                lastMinK = i

            #start of valid subarray
            startOfSubArray = min(lastMinK , lastMaxK)
            #Length of valid subarray
            temp = startOfSubArray - culpritIndex
            res += temp if temp > 0 else 0 

        return res 