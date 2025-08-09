class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def backtrack(i, curAns, cur): 
            if i >= len(num):
                if eval("".join(cur)) == target:
                    res.append("".join(cur))
                return 

            if cur and cur[-1].isdigit():
            #place an operator:
                for operand in "+-*":
                    cur.append(operand)
                    backtrack(i, curAns, cur)
                    cur.pop()
            #extend the num 
                if len(cur[-1]) == 1 and cur[-1] == "0":
                    return
                cur[-1] = str(int(cur[-1] + num[i]))
                backtrack(i + 1, curAns, cur)
            else: 
                backtrack(i + 1, curAns, cur + [num[i]])

            return 

        backtrack(0, 0, [])
        return res




            

