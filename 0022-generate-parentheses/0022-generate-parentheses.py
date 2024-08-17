class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN , closedN):
            if openN == closedN == n : 
                res.append("".join(stack))
                return 

            #We have two options either to choose opened bracket or closed bracket 
            #But if open bracket is less than n , then it is mandatory to have open bracket so we put it first 
            if openN < n : 
                stack.append("(")
                backtrack(openN + 1 , closedN)
                stack.pop() #state restored 
            if closedN < openN : 
                #If closed brackets are less than openN
                stack.append(")")
                backtrack(openN ,closedN + 1)
                stack.pop()
        
        backtrack(0 , 0)
        return res 