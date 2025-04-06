class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for c in s: 
            inside = False
            while stack and stack[-1] == c: 
                stack.pop()
                inside = True 
            if not inside:
                stack.append(c)

        return "".join(stack)