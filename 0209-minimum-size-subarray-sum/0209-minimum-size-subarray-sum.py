class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #Basically , I will take a sliding window  with l and r , r moves right until sum is less than target , the moment subarray becomes greater than or equal to target , l is incremented , this is because at that stage it is the minimum length subarray for which condition is valid 
        l ,r = 0 , 0
        res = float('inf')
        curSum = 0 
        while r < len(nums) :
            curSum += nums[r]
            while curSum >= target : 
                res = min(res, (r-l+1))
                curSum -= nums[l]
                l += 1 
            r+=1 

        return 0 if res == float('inf') else res