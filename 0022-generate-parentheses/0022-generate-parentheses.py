class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #Why not stack ? 
        #Stack can only confirm , for generating we need bactrack 
        #Point 1: start with open 
        res = []
        def backtrack(path, openn): 
            if openn < 0: 
                return 

            if len(path) == n * 2: 
                if openn == 0:
                    res.append(path) 
                return 

            backtrack(path + "(", openn + 1)
            backtrack(path + ")", openn - 1)

        backtrack("(", 1)
        return res


