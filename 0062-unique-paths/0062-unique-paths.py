class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n 

        for i in range(m - 1) :
            #for right most value 
            newRow = [1] * n 
            for j in range(n - 2 , -1 , -1) : 
                #Skipped last value to account for 1 base case at end of each row 
                newRow[j] = newRow[j + 1] + row[j]

            row = newRow

        return row[0]