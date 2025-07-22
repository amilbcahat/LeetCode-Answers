class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        print(n)
        if n == 1 : 
            return True 

        if n == 0: 
            return False 

        if n % 4: 
            return False 
        else: 
            return self.isPowerOfFour(n / 4)