class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:

        stack = []
        for i, n in enumerate(nums): 
            while stack and stack[-1] > n and k > 0: 
                stack.pop()
                k -= 1
            stack.append(n)
        if len(stack) == 1 and k > 0: 
            return "0"

        p1 = -1 
        for i, n in enumerate(stack): 
            if n != "0": 
                p1 = i 
                break 

        st1 = "".join(stack[p1:])

        #Now remember we used a stack, so its always increasing if , len of stack is same as len of string, nothing got deleted
        #So we will remove the right part, as it would be the greatest, and that would make the number smaller 
        return st1 if not k else (st1[:-k] if st1[:-k] else "0")
