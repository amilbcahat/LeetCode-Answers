class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        squaresSet = defaultdict(set)

        di = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        #PreProcess the board
        for r in range(9): 
            for c in range(9): 
                if board[r][c] == ".":
                    continue

                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                squaresSet[(r//3, c//3)].add(board[r][c])


        def backtrack(r, c): 
            if r == n: 
                return True 
            elif c == n: 
                return backtrack(r + 1, 0)

            if board[r][c] != ".": 
                return backtrack(r, c + 1)

            for v in "123456789": 
                if v in rowSet[r] or v in colSet[c] or v in squaresSet[(r//3, c//3)]:
                    continue 

                board[r][c] = v
                rowSet[r].add(v)
                colSet[c].add(v)
                squaresSet[(r//3, c//3)].add(v)

                if backtrack(r, c + 1): 
                    return True 

                board[r][c] = '.'
                rowSet[r].remove(v)
                colSet[c].remove(v)
                squaresSet[(r//3, c//3)].remove(v)

            return False
        
        backtrack(0, 0)



            