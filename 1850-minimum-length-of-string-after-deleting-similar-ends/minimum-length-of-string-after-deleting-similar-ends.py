class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) == 1 : 
            return 1 

        l , r = 0 , len(s) - 1 

        while l < r and s[l] == s[r]:
            
            ch = s[l] 
            while l <= r and s[l] == ch :
                l += 1 
            while r >= l and s[r] == ch :
                r -= 1 

        return r - l + 1
        
