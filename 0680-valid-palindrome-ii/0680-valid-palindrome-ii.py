class Solution:
    def validPalindrome(self, s: str) -> bool:
        N = len(s)
        r = len(s) - 1
        l = 0 

        def helperPali(l, r):
            while l < r: 
                if s[l] != s[r]: 
                    return False 
                l += 1
                r -= 1
            return True 
        
        while l < r: 
            if s[l] != s[r]: 
                return helperPali(l , r - 1) or helperPali(l + 1, r)
            l += 1
            r -= 1
        return True
