class Solution:
    def calculate(self, s: str) -> int:
        #TODO: 
        #1. Convert to Possible Manipulation String 
        i = -0 
        curNum = ""
        arr = []
        while i < len(s): 
            if s[i].isdigit(): 
                curNum += s[i]
                if i == len(s) - 1: 
                    arr.append(curNum)
            else:
                if curNum:
                    arr.append(curNum)
                if s[i] != " ":
                    arr.append(s[i])
                curNum = ""
            i += 1
        print(arr)
        #2. Convert Infix to Postfix 
        precedence = {"+" : 1, "-": 1, "*": 2, "/": 2}
        operators = set(['+', '-', '*', '/'])
        postfix = []
        stack = []
        for c in arr:
            if c.isdigit(): 
                postfix.append(c)
            elif c == "(": 
                stack.append(c)
            elif c == ")": 
                while stack and stack[-1] != "(": 
                    postfix.append(stack.pop())
                stack.pop()

            elif c in operators: 
                while stack and stack[-1] != "(" and precedence.get(c, 0) <= precedence.get(stack[-1], 0): 
                    postfix.append(stack.pop())
                stack.append(c)

        while stack:
            postfix.append(stack.pop())
        print(postfix)

        #3. Evaluate Postfix with stack 
        stack2 = []
        for c in postfix: 
            if c == "+": 
                stack2.append(stack2.pop() + stack2.pop())
            elif c == "-":
                a, b = stack2.pop(), stack2.pop()
                stack2.append(b - a)
            elif c == "*":
                stack2.append(stack2.pop() * stack2.pop())
            elif c == "/":
                a, b = stack2.pop(), stack2.pop()
                stack2.append(int(b / a))
            else:
                stack2.append(int(c))

        return int(stack2[0])