class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax , curMin = 1, 1 

        for n in nums : 
            #Reset when found a zero (although this loop is not necessary )
            if n == 0 : 
                curMax , curMin = 1 , 1 
            oldCurMax = curMax * n
            curMax = max(curMax * n , curMin * n , n)
            curMin = min(oldCurMax , curMin * n  , n)
            res = max(curMax , curMin , res)

        return res 