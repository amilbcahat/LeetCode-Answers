class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            #x raised to any power is zero 
            if x == 0 : 
                return 0 
            #x raised to 0 is 1 
            if n == 0 : 
                return 1 
            #n//2 is taken because 2^10 can be writtern as 2^5*2^5 , hence a divide and conquer approach
            res = helper(x,n//2)
            #2^10 = 2^5 * 2^5, thats why 
            res = res * res 
            #We return x * res if power is odd because 2^5 = 2 * 2^2 * 2^2
            return x * res if n % 2 else res 
        res = helper(x , abs(n))
        #else condition is for handling negative power ! 
        return res if n>=0 else 1/res