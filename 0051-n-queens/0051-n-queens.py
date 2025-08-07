class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for i in range(n)] for i in range(n)]

        posDiag = set()
        negDiag = set()
        col = set()
        res = []
        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return 

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag: 
                    continue      
                col.add(c)              
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"                               
                backtrack(r + 1)                             
                board[r][c] = "."
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(0)

        return res
            
        