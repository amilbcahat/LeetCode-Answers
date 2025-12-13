class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        arr = []

        #level means queen being placed
        def check(c, arr): 
            ri = len(arr)
            for rIdx, colIdx in enumerate(arr):
                if colIdx == c or abs(rIdx - ri) == abs(colIdx - c): 
                    return False

            return True

        def constructArr(arr):
            board = []
            #row
            for r in range(n):
                cur_row = ""
                #col 
                for c in range(n):
                    if c == arr[r]:
                        cur_row += "Q"
                    else:
                        cur_row += "."
                board.append(cur_row)
            return board



        ans = []
        def dfs(level, arr):
            if level == n:
                ans.append(constructArr(arr))
                return 1 

            res = 0
            for colChoice in range(0, n): 
                #
                if check(colChoice, arr):
                    arr.append(colChoice)
                    res += dfs(level + 1, arr)
                    arr.pop()

            return res
        dfs(0, arr)
        return ans


