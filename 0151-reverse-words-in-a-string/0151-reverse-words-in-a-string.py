class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        def nextValid(st):
            i = len(st) - 1 
            while i >= 0 and st[i] == " ": 
                i -= 1 
            return i 

        p1 = len(s) 
        
        while p1 >= 0 : 
            idx = nextValid(s[:p1])
            p1 = idx 
            curRes = ""
            while p1 >= 0 and s[p1] != " ":
                curRes = s[p1] + curRes 
                p1 -= 1 
            res += (curRes + " ") 

        idx = nextValid(res)

        return res[:idx + 1]
