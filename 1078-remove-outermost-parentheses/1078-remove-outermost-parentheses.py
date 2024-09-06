class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res , opened = [] , 0

        for p in s : 
            #This can be taken , by ignoring the first open 
            if p == "(" and opened > 0 : res.append(p)

            #When inside then take when only two or more opens
            if p == ")" and opened > 1 : res.append(p)
            opened += 1 if p == "(" else -1

        return "".join(res)

        