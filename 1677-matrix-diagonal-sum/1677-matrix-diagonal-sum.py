class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows , cols = len(mat) , len(mat[0])

        total = 0 
        for i in range(rows) : 
            for j in range(cols) : 
                if i == j or (j == rows - i - 1) or (i == rows - j - 1): 
                    total += mat[i][j]

        return total
        