class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        # Similar to approach 3, if we fix k, then the value of the triplet is maximized when nums[i]−nums[j] takes the maximum value. We can use imax to maintain the maximum value of nums[i] and dmax to maintain the maximum value of nums[i]−nums[j]. During the enumeration of k, update dmax and imax.
        n = len(nums)
        res, imax, dmax = 0, 0, 0
        for k in range(n):
            res = max(res, dmax * nums[k])
            dmax = max(dmax, imax - nums[k])
            imax = max(imax, nums[k])
        
        return res

        #Takes space
        # n = len(nums)
        # leftMax = [0] * n 
        # rightMax = [0] * n
        # res = 0
        # #Greedify left and right, for mid , you can search max 
        # for i in range(1 , n): 
        #     leftMax[i] = max(leftMax[i - 1], nums[i - 1])
        #     rightMax[n - i - 1] = max(rightMax[n - i], nums[n - i])

        # for j in range(1, n - 1):
        #     res = max(res, (leftMax[j] - nums[j]) * rightMax[j])

        # return res 

        #Mine Solution , takes space
        # buyPrice = nums[0]
        # r = -1
        # l = 0
        # loss = 0
        # nextBig = 1
        # rightMax = float("-inf")
        # res = float("-inf")
        # maxElem = [0] * len(nums)
        # curMax = nums[-1]
        # #Suffix array of maximums 
        # for j in range(len(nums) - 1, -1 ,-1):
        #     curMax = max(curMax, nums[j])
        #     maxElem[j] = curMax 

        # #Intuition of Buy and Sell Stock but here , we search for max loss (nums[i] higher and nums[j] lower)
        # for i, n in enumerate(nums): 
        #     if buyPrice < n: 
        #         buyPrice = n 
        #         l = i
            
        #     if loss < buyPrice - n:
        #         loss = buyPrice - n
        #         r = i
        #     #When found a loss maximize , the score by multiply the greatest elem from right side of r 
        #         if loss != 0 and r + 1 < len(nums):
        #             print(l , r, rightMax, loss)
        #             rightMax = maxElem[r + 1]
        #             res = max(loss * rightMax, res)

        # return res if res != float("-inf") else 0
