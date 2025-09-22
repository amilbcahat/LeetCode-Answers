class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        #Convert Matrix to Histograms
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows): 
            for c in range(cols): 
                matrix[r][c] = int(matrix[r][c])

        for r in range(1, rows): 
            for c in range(cols): 
                if matrix[r][c] == 0: 
                    continue 
                else: 
                    matrix[r][c] = matrix[r][c] + matrix[r - 1][c]

        #ALGORITHM for largest rectange in histogram
        def getMaxForRow(arr): 
            stack = []
            maxArea = float("-inf")
            for i, h in enumerate(arr): 
                start = i
                while stack and stack[-1][1] > h: 
                    index, height = stack.pop()
                    maxArea = max(maxArea, height * (i - index))

                    start = index 
                stack.append((start, h))

            for i, h in stack: 
                maxArea = max(maxArea, h * (len(arr) - i))

            return maxArea

        #Calculate the most max for each row of histogram
        res = 0
        for row in matrix: 
            res = max(res, getMaxForRow(row))

        return res
