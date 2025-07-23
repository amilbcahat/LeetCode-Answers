class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        print(n)
        if n <= 0: 
            return False 

        if n == 1: 
            return True 

        if n % 3 == 0: 
            return self.isPowerOfThree(n // 3)
        else: 
            return False