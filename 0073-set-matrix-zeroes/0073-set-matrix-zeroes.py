class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows , cols = len(matrix) , len(matrix[0])
        rowZero = False 
        
        #Same way as before but here , we follow left to right approach 
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0 : 
                    #Mark corresponding 0 in first row as 0 
                    matrix[0][c] = 0 
                    # col is first col then mark them as zero 
                    if r > 0 : 
                        matrix[r][0] = 0 
                    else : 
                    #If first row contains zero 
                        rowZero = True 
        
        #Mark zeroes in other rows and cols other than first row and first col
        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0 : 
                    matrix[r][c] = 0 

        #If first element is zero , then mark entire first col as zero 
        if matrix[0][0] == 0 :
            for r in range(rows):
                matrix[r][0] = 0 
        #If first row iz zero then mark that row as zero 
        if rowZero : 
            for c in range(cols):
                matrix[0][c] = 0 