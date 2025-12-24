class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        leftMin = 0 
        leftMax = 0 

        if len(s) & 1: 
            return False

        

        for i, c in enumerate(s): 
            if locked[i] == "1":
                if c == "(": 
                    leftMin += 1
                    leftMax += 1 
                elif c == ")": 
                    leftMin -= 1 
                    leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1

            if leftMax < 0: 
                return False 

            if leftMin < 0:
                leftMin = 0 

        return leftMin == 0


            