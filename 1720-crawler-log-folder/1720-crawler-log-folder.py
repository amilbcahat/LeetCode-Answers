class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for log in logs : 
            if log == "../" : 
                if stack : 
                    stack.pop()
                else: 
                    continue
            elif log == "./" :
                continue 
            else : 
                stack.append(log)

        print(stack)
        return len(stack)
