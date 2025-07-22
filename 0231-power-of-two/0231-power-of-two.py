class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def poww(n):
            print(n)
            if n == 1: 
                return True   
            if n == 0: 
                return False              

            res = False
            if (n & 1): 
                #odd
                return False 
            else: 
                res = res or poww(n // 2)

            return res 

        return poww(n)