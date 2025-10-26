class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l = 0 
        r = (rows * cols) - 1

        while l <= r: 
            mid = (l + r) // 2
            cr = mid // cols 
            cc = mid - (cr * cols)
            if matrix[cr][cc] == target: 
                return True 
            elif target <= matrix[cr][cc]: 
                r = mid - 1
            else: 
                l = mid + 1

        return False