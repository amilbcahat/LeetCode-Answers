class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openn = 0
        close = 0 
        neverClosed = 0
        for b in s: 
            if b == "(":
                openn += 1
            else: 
                openn -= 1

            if openn < 0: 
                neverClosed = min(neverClosed, openn)

            # print(openn)
            
        # print("open", openn, "neverClosed", neverClosed)
        #When openn == neverClosed
        #   Only never closed brackets would be there
        #if open > neverClosed: 
        #   There are -neverClosed brackets and open - neverClosed, open brackets
        return (-neverClosed) + (openn - neverClosed)