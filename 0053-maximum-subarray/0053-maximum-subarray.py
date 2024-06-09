class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0 

        for n in nums : 
            curSum += n 
            #This below statements checks the right pointer kinda and puts the pointer wherever sum is max for a subarray
            maxSub = max(maxSub,curSum)
            #This if statement works as left pointer , incase , the curSum evaluates to negative then its useless , hence we update it to 0 and start again 
            if curSum < 0 : 
                curSum = 0 

        return maxSub 