class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s: 
            duplicate = False
            while stack and stack[-1] == c: 
                stack.pop()
                duplicate = True 
            if not duplicate:
                stack.append(c)

        return "".join(stack)