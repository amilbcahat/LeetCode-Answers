class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Striver Solution -> 
        #Flatten to 1D Array then solve 
        rows , cols = len(matrix) , len(matrix[0])
        l , r = 0 , (rows * cols)- 1

        while l <= r : 
            mid = (l + r) // 2 

            #We flatten to 1D array by this logic always 
            row = mid // cols 
            col = mid % cols 

            if matrix[row][col] > target : 
                r = mid - 1
            elif matrix[row][col] < target : 
                l = mid + 1
            else : 
                return True
        return False 

        #NeetCode solution -> 
        # rows , cols = len(matrix) , len(matrix[0])

        # top = 0
        # bot = rows - 1

        # while top <= bot : 
        #     row = (top + bot) // 2 
        #     if target > matrix[row][-1] : 
        #         top = row + 1
        #     elif target < matrix[row][0] : 
        #         bot = row - 1 
        #     else : 
        #         break 

        # if top > bot : 
        #     return False 

        # l , r = 0 , cols - 1
        # while l <= r : 
        #     mid = (l + r) // 2 
        #     if target > matrix[row][mid] : 
        #         l = mid + 1 
        #     elif target < matrix[row][mid] : 
        #         r = mid - 1
        #     else : 
        #         return True 
        # return False 