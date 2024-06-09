class Solution:
    def mySqrt(self, x: int) -> int:
        ##neetcode solution 
        l , r = 1 , x 
        res = 0
        while l <= r : 
            
            mid = (l + (r - l) // 2)
            
            if mid ** 2 == x : 
                return mid 
            elif mid ** 2 < x : 
                l = mid + 1 
                #Could be the ans
                res = mid 
            else : 
                r = mid - 1 
        return res 

