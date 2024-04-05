class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for n in s : 
            if stack and abs(ord(stack[-1]) -  ord(n )) == 32:
                stack.pop()
            else : 
                stack.append(n)
            

        return "".join(stack)