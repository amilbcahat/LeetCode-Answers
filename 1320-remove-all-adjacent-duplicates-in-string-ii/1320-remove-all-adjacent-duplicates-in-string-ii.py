class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        s += "-1" #Just added this , so last char gets considered as well for popping out
        for c in s:
            if stack and stack[-1][1] == k : 
                t = k
                while stack and t > 0: 
                    stack.pop()
                    t -=  1
            adj = 1
            if stack:
                if stack[-1][0] == c: 
                    adj = stack[-1][1] + 1
                else: 
                    adj = 1
            stack.append((c, adj))
        return "".join([c for c, adj in stack[:-2]]) #Just take result before -1