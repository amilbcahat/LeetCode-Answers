class Solution:
    def minCut(self, s: str) -> int:
        
        memoPali = {}
        def isValidPali(start, end):
            if start >= end: 
                return True 

            if s[start] != s[end]: 
                return False

            if (start, end) in memoPali: 
                return memoPali[(start, end)]

            memoPali[(start, end)] = isValidPali(start + 1, end - 1)

            return memoPali[(start, end)]



        memo = {}
        def backtrack(i): 
            if i >= len(s):
                return -1

            if i in memo: 
                return memo[i]

            res = float("inf")
            for j in range(i, len(s)):                         
                if isValidPali(i, j):                   
                    res = min(res, 1 + backtrack(j + 1))

            memo[i] = res

            return res

        return backtrack(0)
        