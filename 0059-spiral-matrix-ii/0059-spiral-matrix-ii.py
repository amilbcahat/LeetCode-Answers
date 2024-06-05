class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        answer = [i + 1 for i in range(n * n)]
        matrix = [[0] * n for _  in range(n)]
        print(answer , matrix)
        top , bottom = 0 , len(matrix)
        left , right = 0 , len(matrix[0])

        y = 0 
        while top < bottom and left < right : 

            for i in range(left , right):
                matrix[top][i] = answer[y]
                y += 1 
            top += 1 

            for i in range(top , bottom):
                matrix[i][right - 1] = answer[y]
                y += 1 
            right -= 1

            if bottom > top and left > right :
                break 

            for i in range(right - 1 , left - 1, -1):
                matrix[bottom - 1][i] = answer[y]
                y += 1 
            bottom -= 1 

            for i in range(bottom - 1 , top -1 , -1):
                matrix[i][left] = answer[y]
                y += 1 
            left += 1 
        return matrix