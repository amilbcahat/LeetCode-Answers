class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Start from Top Right Corner 
        #To find greater number , search downwards (row ++)
        #To find lesser number , search leftwards (cols --)
        rows , cols = len(matrix) , len(matrix[0])
        row , col = 0 , len(matrix[0]) - 1

        while row < rows and col >= 0 : 
            if matrix[row][col] < target : 
                row += 1 
            elif matrix[row][col] > target : 
                col -= 1 
            else : 
                return True 
        
        return False 