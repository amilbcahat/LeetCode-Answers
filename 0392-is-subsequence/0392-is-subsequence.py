class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i , j = 0 , 0 

        while i < len(s) and j < len(t) : 
            if s[i] == t[j] : 
                i , j = i + 1 , j + 1
            else : 
                #Look for some parts of s in t 
                j += 1 
        
        return len(s) == i 