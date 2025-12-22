class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        curMin , curMax = 1 , 1 

        for n in nums : 
            #Reset when found a zero (although this loop is not necessary )
            if n == 0:
                curMin, curMax = 1, 1
                continue

            #Tuple assignment -> Dont require extra oldMax var
            curMax, curMin = max(n*curMax, n*curMin, n), min(n*curMax, n*curMin, n)

            res = max(res, curMax)
        return res 
        