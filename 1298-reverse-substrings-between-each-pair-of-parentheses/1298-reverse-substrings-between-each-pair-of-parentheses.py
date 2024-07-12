class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        #O(n * m)
        #check with testcase 3 
        for c in s : 
            if c == ")" : 
                portion = []
                while stack and stack[-1] != "(" :
                    #pops only char here  
                    #oc changes to co
                    #Reverses the inner bracket string as well when popping 
                    portion.append(stack.pop())
                #Pops open bracket
                stack.pop()
                #Then append like etco , same happens recursively
                stack.extend(portion)
                print(stack)
            else : 
                stack.append(c)

        return "".join(stack)