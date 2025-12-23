class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #First we did DFS specially for boundary "O" and added adjacent "O" in visit set , then traversed whole matrix again and if there is a "O" , that is not in visit ,then it is flipped ! 
        rows, cols = len(board), len(board[0])
        visit = set()
        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or board[r][c] == "X" or (r, c) in visit:
                return 

            visit.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0 or c == cols - 1 or r == rows - 1:
                    dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and board[r][c] == "O":
                    board[r][c] = "X"
