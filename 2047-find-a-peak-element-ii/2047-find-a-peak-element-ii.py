class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        #Intuition is similar to that of Find Peak Element 
        #The reason binary search works here even when its not sorted, is because , we are getting any peak element , and not the maximum peak element 
        rows , cols = len(mat) , len(mat[0])
        l , r = 0 , cols - 1

        def maxElement(col) : 
            maxIndx = -1 
            maxElem = float("-inf")
            for i in range(rows):
                if mat[i][col] > maxElem : 
                    maxRowIndx = i 
                    maxElem = mat[i][col]
            return maxRowIndx

        #Row Wise , we get a mid column 
        while l <= r : 
            mid = (l + r) // 2 
            #We get the maxElement index for that column (it assures a better rate of finding an element , that is peak , since it would be greater than top element and bottom element)
            row = maxElement(mid)

            #Get the left and right elements ,else consider them -1
            left = mat[row][mid - 1] if mid > 0 else -1 
            right = mat[row][mid + 1] if mid < len(mat[row]) - 1 else -1 

            #If left is at greater height , then means peak is there (inclination is better)
            if mat[row][mid] < left : 
                r = mid - 1
            #Same logic just for right side 
            elif mat[row][mid] < right : 
                l = mid + 1
            else : 
                return [row , mid]
        return [-1 , -1]

