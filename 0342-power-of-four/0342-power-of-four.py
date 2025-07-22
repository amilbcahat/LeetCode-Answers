class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        #Check Editorials for awesome bit tricks 
        return num > 0 and num & (num - 1) == 0 and num % 3 == 1