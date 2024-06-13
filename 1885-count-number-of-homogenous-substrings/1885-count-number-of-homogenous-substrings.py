class Solution:
    def countHomogenous(self, s: str) -> int:
        # a = 1 
        # bb = 1 + 2 = 3  
        # ccc = 1 + 2 + 3 = 6 
        # aa = 1 + 2 = 3 

        #Basically just add them according to the patterns 

        res , l = 0 , 0 

        for r , c in enumerate(s):
            if c == s[l]:
                res += (r - l + 1)
            else : 
                l = r 
                res += 1 

        return res % (10 ** 9 + 7)