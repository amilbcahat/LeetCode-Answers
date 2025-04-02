class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        buyPrice = nums[0]
        r = -1
        l = 0
        loss = 0
        nextBig = 1
        res = float("-inf")
        for i, n in enumerate(nums): 
            if buyPrice < n: 
                buyPrice = n 
                l = i
            
            if loss < buyPrice - n:
                loss = buyPrice - n
                r = i
                if loss != 0 and r + 1 < len(nums):
                    print(l , r)
                    nextBig = max(nums[r + 1:])
                    res = max(loss * nextBig, res)
        return res if res != float("-inf") else 0
        # print(l , r)
        # if loss == 0 or r + 1 >= len(nums): 
        #     # print(r, loss)
        #     return 0

        

        return 0
