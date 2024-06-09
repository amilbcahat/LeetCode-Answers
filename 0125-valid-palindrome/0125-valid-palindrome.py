class Solution:
    def isPalindrome(self, s: str) -> bool:
        l , r = 0 , len(s) - 1
        while l < r :
            while l < r and not self.alphaNum(s[l]):
                l += 1 
            while l < r and not self.alphaNum(s[r]):
                r -= 1 

            if s[l].lower() != s[r].lower():
                return False 
            l += 1 
            r -= 1 
        return True 

        
    def alphaNum(self , s):
        return (ord("A") <= ord(s) <= ord("Z") or 
        ord("a") <= ord(s) <= ord("z") or 
        ord("0") <= ord(s) <= ord("9"))