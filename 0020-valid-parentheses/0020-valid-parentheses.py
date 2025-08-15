class Solution:
    def check(self, top, c): 
        if top == "(" and c == ")": 
            return True 
        elif top == "{" and c == "}":
            return True 
        elif top == "[" and c == "]": 
            return True 

        return False


    def isValid(self, s: str) -> bool:
        if len(s) == 1: 
            return False 

        stack = []
        skip = False
        for c in s: 
            if stack and self.check(stack[-1], c): 
                stack.pop()
                skip = True 

            if not skip: 
                stack.append(c)
            skip = False

        return True if not stack else False