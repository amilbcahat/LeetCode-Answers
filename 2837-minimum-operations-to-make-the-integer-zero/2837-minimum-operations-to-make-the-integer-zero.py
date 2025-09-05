class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
#           Solution - https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/solutions/7156791/beats-100-0ms-bit-manipulation-full-explanation
        if num1 == 0: 
            return 0

        for t in range(0, 61): 
            s = num1 - (t * num2)

            if s < 0: 
                continue 
            if t > s: 
                continue 

            ones = s.bit_count()
            if ones <= t: 
                return t 

        return -1