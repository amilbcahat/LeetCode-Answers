class Solution:
    def minOperations(self, logs: List[str]) -> int:
        #Can be done with Stack as well , p is depth
        p = 0 

        for log in logs : 
            if log == "../" : 
                if p > 0 : 
                    p -= 1
                else: 
                    continue
            elif log == "./" :
                continue 
            else : 
                p += 1

        
        return p
        # stack = []

        # for log in logs : 
        #     if log == "../" : 
        #         if stack : 
        #             stack.pop()
        #         else: 
        #             continue
        #     elif log == "./" :
        #         continue 
        #     else : 
        #         stack.append(log)

        # print(stack)
        # return len(stack)
