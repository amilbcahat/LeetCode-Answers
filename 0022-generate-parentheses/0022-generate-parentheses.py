class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #Why not stack ? 
        #Stack can only confirm , for generating we need bactrack 
        # backtrack 
        res = []
        def backtrack(path, left_count, right_count): 
            if len(path) == n * 2: 
                res.append("".join(path))
                return 

            if left_count < n: 
                path.append("(")
                backtrack(path, left_count + 1, right_count) 
                path.pop()

            if left_count > right_count: 
                path.append(")")
                backtrack(path, left_count, right_count + 1)
                path.pop()

        backtrack([], 0, 0)

        return res

        #Point 1: start with open , recursion 
        # res = []
        # def backtrack(path, openn): 
        #     if openn < 0: 
        #         #closed bracket has some point dominated open, thats why
        #         return 

        #     if len(path) == n * 2: 
        #         if openn == 0:
        #             res.append(path) 
        #         return 

        #     backtrack(path + "(", openn + 1)
        #     backtrack(path + ")", openn - 1)

        # backtrack("(", 1)
        # return res


