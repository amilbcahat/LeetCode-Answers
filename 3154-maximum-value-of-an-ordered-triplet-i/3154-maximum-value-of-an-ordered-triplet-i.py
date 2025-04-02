class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        buyPrice = nums[0]
        r = -1
        l = 0
        loss = 0
        nextBig = 1
        res = float("-inf")
        greatElem = [0] * len(nums)
        curMax = nums[-1]
        for j in range(len(nums) - 1, -1 ,-1):
            curMax = max(curMax, nums[j])
            greatElem[j] = curMax 

        for i, n in enumerate(nums): 
            if buyPrice < n: 
                buyPrice = n 
                l = i
            
            if loss < buyPrice - n:
                loss = buyPrice - n
                r = i
                if loss != 0 and r + 1 < len(nums):
                    print(l , r)
                    nextBig = greatElem[r + 1]
                    res = max(loss * nextBig, res)

        return res if res != float("-inf") else 0
