class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for n in tokens : 
            if n == "+" : 
                elm1 , elm2 = stack.pop() , stack.pop()
                stack.append(int(elm1) + int(elm2))
            elif n == "-" : 
                elm1 , elm2 = stack.pop() , stack.pop()
                stack.append(int(elm2) - int(elm1))
            elif n == "/" : 
                elm1 , elm2 = stack.pop() , stack.pop()
                stack.append(int(int(elm2) / int(elm1)))
            elif n == "*" : 
                elm1 , elm2 = stack.pop() , stack.pop()
                stack.append(int(elm1) * int(elm2))
            else : 
                stack.append(int(n))

        return stack[-1]