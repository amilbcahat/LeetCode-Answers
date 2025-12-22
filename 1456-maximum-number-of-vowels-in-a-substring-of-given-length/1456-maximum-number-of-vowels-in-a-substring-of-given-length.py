class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a" , "e" , "i" , "o" , "u"}

        l = 0 
        cur = 0 
        res = 0 
        for r in range(len(s)):
            cur += 1 if s[r] in vowels else 0 
            
            while (r - l + 1) > k : 
                cur -= 1 if s[l] in vowels else 0 
                l += 1 

            res = max(cur , res)

        return res   