class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin , curMax = 1 , 1

        for n in nums : 
            
            #Reset when found a zero (although this loop is not necessary )
            if n == 0 : 
                curMin , curMax = 1 , 1 
            
            oldCurMax = curMax * n 
            curMax = max(n * curMax , n * curMin , n)
            curMin = min(oldCurMax , n * curMin , n)
            res = max(curMax , res , curMin)

        return res 
        