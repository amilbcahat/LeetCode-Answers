class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0 
        #Logic is that we take XOR of everything 
        #Then match with K , to flip we require to flip only one bit (minimum)(mess up even count of 0s and 1s or odd count of 0s and 1s)
        for i in nums : 
            ans = ans ^ i 

        #Now we find where the mismatch 
        diff = ans ^ k 

        #Count the mismatches !
        res = 0 
        while diff:
            diff = diff & (diff - 1)
            res += 1 

        return res  