class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows , cols = len(board) , len(board[0])
        visit = set() 
        def dfs(r , c) : 
            if (r , c) in visit or r not in range(rows) or c not in range(cols) or board[r][c] == "X" : 
                return 

            visit.add((r  , c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r , c+ 1)
            dfs(r , c - 1)

        for r in range(rows) : 
            for c in range(cols) : 
                if r == 0 or c == 0 or c == cols - 1 or r == rows - 1 : 
                    dfs(r , c)

        for r in range(rows):
            for c in range(cols) : 
                if (r , c) not in visit and board[r][c] == "O" : 
                    board[r][c] = "X"