class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l , r = 0 , len(matrix) - 1 

        while l < r : 
            for i in range(r-l):
                top , bottom = l , r 
                #Reverse 90 degree value exchange for code to be simpler 
                 # save the topleft
               
                topleft = matrix[top][l + i]
                # move bottom left into top left

                matrix[top][l + i] = matrix[bottom - i][l]
                # move bottom right into bottom left

                matrix[bottom - i][l] = matrix[bottom][r - i ]
            # move top right into bottom right

                matrix[bottom][r - i] = matrix[top + i][r] 
             # move top left into top right

                matrix[top + i][r] = topleft
            l+=1
            r-=1

    #     class Solution:
            # def rotate(self, matrix: List[List[int]]) -> None:
            #     #Find Transpose 
            #     for i in range(len(matrix)):
            #         for j in range(i+1,len(matrix)):
            #             matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
                
            #     #Then Reverse it 
            #     for i in range(len(matrix)):
            #         matrix[i].reverse()