class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        buyPrice = nums[0]
        r = -1
        l = 0
        loss = 0
        nextBig = 1
        rightMax = float("-inf")
        res = float("-inf")
        maxElem = [0] * len(nums)
        curMax = nums[-1]
        #Suffix array of maximums 
        for j in range(len(nums) - 1, -1 ,-1):
            curMax = max(curMax, nums[j])
            maxElem[j] = curMax 

        #Intuition of Buy and Sell Stock but here , we search for max loss (nums[i] higher and nums[j] lower)
        for i, n in enumerate(nums): 
            if buyPrice < n: 
                buyPrice = n 
                l = i
            
            if loss < buyPrice - n:
                loss = buyPrice - n
                r = i
            #When found a loss maximize , the score by multiply the greatest elem from right side of r 
                if loss != 0 and r + 1 < len(nums):
                    print(l , r, rightMax, loss)
                    rightMax = maxElem[r + 1]
                    res = max(loss * rightMax, res)

        return res if res != float("-inf") else 0
