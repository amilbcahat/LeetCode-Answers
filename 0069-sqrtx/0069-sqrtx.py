class Solution:
    def mySqrt(self, x: int) -> int:
        l , r = 1 , x 

        while l <= r : 
            
            mid = (l + r) // 2
            target = x // mid 

            print(l ,r , mid , target)
            if target == mid : 
                return mid 
            elif target > mid : 
                l = mid + 1 
            else : 
                r = mid - 1 
        return r 

