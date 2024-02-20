class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #Solution - 3 (Prime Factorisation !) 32 bit largest 2 number % (input) is 0 
        return n > 0 and ((1 << 30) % n ) == 0 
        # Solution -2 
        # return n > 0 and n & n - 1 == 0 
        # Solution - 1
        # x = 1 
        # while x < n : 
        #     x*= 2 
        # return x == n 