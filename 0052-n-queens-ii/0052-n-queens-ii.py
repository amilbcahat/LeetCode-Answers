class Solution:
    def totalNQueens(self, n: int) -> int:
        # board = [["." for _ in range(n)]] * n 

        # print(board)
        #check for Nqueens condition 
        #[0, 0, 0, 0] <- place different queen at diff i pos , arr will be mapped like arr[ri] -> coli 

        arr = []

        #level means queen being placed
        def check(c, arr): 
            ri = len(arr)
            for rIdx, colIdx in enumerate(arr):
                if colIdx == c or abs(rIdx - ri) == abs(colIdx - c): 
                    return False

            return True


        def dfs(level, arr):
            if level == n:
                return 1 

            res = 0
            for colChoice in range(0, n): 
                #
                if check(colChoice, arr):
                    arr.append(colChoice)
                    res += dfs(level + 1, arr)
                    arr.pop()

            return res

        return dfs(0, arr)


