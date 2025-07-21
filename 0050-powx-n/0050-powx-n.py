class Solution:
    def myPow(self, x: float, n: int) -> float:
        def poww(x, n):
            if n == 0: 
                return 1
            res = self.myPow(x, n // 2)
            if(n & 1): #odd
                return x * res * res 
            else: 
                return res * res

        return poww(x, abs(n)) if n > 0 else 1 / poww(x, abs(n)) 
