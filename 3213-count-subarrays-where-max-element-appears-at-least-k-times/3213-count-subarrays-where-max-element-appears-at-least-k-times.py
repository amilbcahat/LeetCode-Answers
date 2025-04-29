class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxElem = max(nums)
        l = 0
        count = 0 
        res = 0 
        n = len(nums)

        #Atleast pattern for sliding window
        for r in range(len(nums)):
            count += 1 if nums[r] == maxElem else 0 
            while l <= r and count >= k:
                res += len(nums) - r

                count -= 1 if nums[l] == maxElem else 0
                l += 1 

        return res