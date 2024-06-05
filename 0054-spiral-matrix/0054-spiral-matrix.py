class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left , right = 0 , len(matrix[0])
        top , bottom = 0 , len(matrix)

        res = []

        #Once we print the cur row or column value we shrink the matrix by top+=1 , bottom-=1 , left+=1 and right-=1

        while left < right and top < bottom : 
            

            #Get top row (left to right)
            for i in range(left,right):
                res.append(matrix[top][i])
            top+=1
            
            #Get right column (top to bottom)
            for i in range(top , bottom):
                res.append(matrix[i][right-1])
            right-=1 

            #If we got all the elements in res !
            if len(res) == (len(matrix)*len(matrix[0])):
                break
            
            #Get bottom row (right to left)
            for i in range(right-1,left -1 , -1):
                res.append(matrix[bottom-1][i])
            bottom-=1 

            #Get left column (bottom to top)
            for i in range(bottom-1 , top-1 , -1):
                res.append(matrix[i][left])
            left+=1 

        return res 