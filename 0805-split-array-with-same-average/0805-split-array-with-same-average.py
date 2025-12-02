class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        from fractions import Fraction 
        n = len(nums)
        s = sum(nums)

        A = [z - Fraction(s, n) for z in nums]

        if n ==1: 
            return False

        #SUBSET SUM, EASY
        left = {A[0]}
        for i in range(1, n//2): 
            left = {z + A[i] for z in left} | left | {A[i]}
        if 0 in left: 
            return True

        right = {A[-1]}
        for i in range(n//2, n - 1): 
            right = {z + A[i] for z in right} | right | {A[i]}
        if 0 in right: 
            return True

        sleft = sum(A[i] for i in range(n // 2))
        sright = sum(A[i] for i in range(n // 2, n))

        return any(-ha in right and (ha, -ha) != (sleft, sright) for ha in left)

