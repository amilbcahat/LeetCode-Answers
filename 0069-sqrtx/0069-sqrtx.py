class Solution:
    def mySqrt(self, x: int) -> int:



        l , r = 1 , x 

        while l <= r : 
            mid = l + (r - l) // 2 
            target = x // mid 

            if target == mid : 
                return mid 
            elif target > mid : 
                l = mid + 1 
            else : 
                r = mid - 1 
        #Return floor value if not found 
        return r