class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # if not matrix:
        #     return

        rowFirstHasZero = False 
        colFirstHasZero = False 

        rows, cols = len(matrix), len(matrix[0])

        #Check for zero in first row -> 
        for i in range(cols):
            if matrix[0][i] == 0 : 
                rowFirstHasZero = True 

        #Check for zero in first col ->
        for j in range(rows):
            if matrix[j][0] == 0 : 
                colFirstHasZero = True 


        #Use first row and first col has cache for storing zeroes 
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        #If 0 in first row or col , mark that col and row with zeroes 
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        print(rowFirstHasZero , colFirstHasZero)
        
        #If The first row had a zero initially make it full of zeroes 
        if rowFirstHasZero : 
            matrix[0] = cols*[0] 

        #If The first col had a zero initially make it full of zeroes 
        if colFirstHasZero : 
            for i in range(rows) :
                matrix[i][0] = 0 