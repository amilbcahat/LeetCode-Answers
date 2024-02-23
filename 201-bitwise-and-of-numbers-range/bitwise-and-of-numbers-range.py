class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0 

        #Logic is simple , we check for the first prefix bit number is same in the range left and right , 
        #This will tell that there is no possibility of a zero alternation zero now , after this prefix 
        #Then make all elements after prefix zero , as they will be zero(when ANDed , it will zero them)
        while left != right : 
            left = left >> 1 
            right = right >> 1 
            i += 1 

        return left << i #Number without zero , when anded 