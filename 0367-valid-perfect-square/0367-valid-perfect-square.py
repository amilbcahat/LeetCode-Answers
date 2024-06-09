class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: 
            return True  

        l , r = 0 , num // 2

        while l <= r : 
            mid = (l + r) // 2 
            if mid * mid == num : 
                return True 
            elif mid * mid < num : 
                l = mid + 1 
            else : 
                r = mid - 1

        return False 