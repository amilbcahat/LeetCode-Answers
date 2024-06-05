class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows , cols = len(matrix) , len(matrix[0])

        ans = [[0] * rows for _ in range(cols)]


        for i in range(cols):
            for j in range(rows):
                ans[i][j] = matrix[j][i]

        return ans 
        #Intuition
# The transpose of a matrix can be obtained by swapping its rows and columns. We iterate through each element of the original matrix and fill the corresponding position in the transposed matrix.

# Approach
# Determine the number of rows (row) and columns (col) in the original matrix.
# Create a new matrix arr with dimensions col x row.
# Iterate through each element of the original matrix, assigning it to the corresponding position in the transposed matrix.
# Return the transposed matrix.
# Complexity
# Time Complexity: O(m * n) where m and n are the number of rows and columns in the matrix.
# Space Complexity: O(m * n) for the transposed matrix.
# Code