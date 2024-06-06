class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ROWS , COLS = len(matrix) , len(matrix[0])

        prev_heights = [0] * COLS 
        res = 0 
        for r in range(ROWS):
            #traverse each row 
            heights = matrix[r][::]
            #Sum up the heights , above the row 
            for c in range(COLS):
                if heights[c] > 0 : 
                    heights[c] += prev_heights[c]

            sorted_heights = sorted(heights , reverse = True)
            
            for i in range(COLS):
                #Take out the maximum area 
                res = max(res , (i + 1) * sorted_heights[i])
            prev_heights = heights 

        return res  