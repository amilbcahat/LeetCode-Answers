class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitsToChar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return 

            for char in digitsToChar[digits[i]]:
                backtrack(i + 1, curStr + char)

        if digits : 
            backtrack(0 , "")
        return res 