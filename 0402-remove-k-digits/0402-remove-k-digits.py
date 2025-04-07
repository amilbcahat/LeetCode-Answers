class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        #Using Monotonic Stack to remove the greater elements
        stack = []
        for i, n in enumerate(nums): 
            while stack and stack[-1] > n and k > 0: 
                stack.pop()
                k -= 1
            stack.append(n)
            
        p1 = -1 
        for i, n in enumerate(stack): 
            if n != "0": 
                p1 = i 
                break 

        st1 = "".join(stack[p1:])

        #Now remember we used a stack, so its always increasing, the greatest is always at the right, now if k > 0, we can still go ahead and delete more 
        #So we will remove the right part, as it would be the greatest, and that would make the number smaller 
        return st1 if not k else (st1[:-k] if st1[:-k] else "0") #Nested ternary to handle the case if string is "" then return "0"
