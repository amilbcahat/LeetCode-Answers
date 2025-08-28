class Solution:
    def decodeString(self, s: str) -> str:
        #2 Stack 
        times = []
        stack = [[]]
        k = 0
        for c in s: 
            if c.isnumeric(): 
                k = int(c) + k * 10
            elif c == "[": 
                times.append(k)
                stack.append([])
                k = 0
            elif c == "]": 
                #decode
                stack[-2].extend(times[-1] * stack[-1])
                stack.pop()
                times.pop()
            else:
                stack[-1].append(c)
        
        print(stack)
        return "".join(stack[-1])



        #1 Stack 
        # stack = []

        # ans = ""
        # for c in s: 
        #     decode = ""
        #     if c == "]": 
        #         while stack and stack[-1] != "[": 
        #             decode = stack.pop() + decode

        #         multi = ""
        #         if decode: 
        #             stack.pop() #Pop [
        #             while stack and stack[-1].isdigit(): 
        #                 multi = stack.pop() + multi #Build multiplier
                    
        #             stack.append(int(multi) * decode) #decode the string of this part
                    
        #     if c != "]": 
        #         stack.append(c)

        # return "".join(stack)


    # # #### SOLUTION 3, RECURSION ######################
    #     """
    #     In this approach, we loop through s and  keep track of current idx, whenever we reach a '[', 
    #     recursively call the function with a new index (one greater than current) and when we reach a ']'
    #     return decoded string so far and one index greater than current index (next index to check).
    #     """

    #     def recur(idx):
    #         multiplier = 0
    #         decoded_str = ''

    #         # loop until length is exhausted or ']' is reached
    #         while idx < len(s) and s[idx] != ']' :

    #             if s[idx].isdigit():
    #                 multiplier = multiplier*10 + int(s[idx])

    #             elif s[idx] == '[':
    #                 # update idx and recurse
    #                 decoded_returned, next_non_closed_bracket_idx = recur(idx+1)
    #                 decoded_str += multiplier * decoded_returned

    #                 # reset multiplier 
    #                 multiplier = 0
    #                 # update the position, to avoid checking what we already checked
    #                 idx = next_non_closed_bracket_idx 

    #             else: # if s[pos] is alphabet
    #                 decoded_str += s[idx]

    #             idx += 1 # when loop ends, this is equal to length of s or index of ']'

    #         # return decoded_str and the idx of ']' in the current recursion
    #         return decoded_str, idx  

    #     return recur(idx=0)[0] # return only the decoded string 