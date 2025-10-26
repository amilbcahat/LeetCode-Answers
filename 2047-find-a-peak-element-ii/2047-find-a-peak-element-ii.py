class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        di = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        def valid(r, c): 
            return (0 <= curR < rows) and (0 <= curC < cols)

        for r in range(rows): 
            for c in range(cols): 
                flag = True 
                for dr, dc in di: 
                    curR = r + dr 
                    curC = c + dc
                    print(curR, curC, valid(curR, curC))
                    if valid(curR, curC) and mat[curR][curC] > mat[r][c]: 
                        flag = False
                        break
                    
                if flag: 
                    return [r, c]

                # break

                # if r - 1 >= 0: 
                #     if mat[r - 1][c] > mat[r][c]: 
                #         flag = False 
                # if r + 1 < rows: 
                #     if mat[r  + 1][c] > mat[r][c]: 
                #         flag = False 
                # if c - 1 >= 0: 
                #     if mat[r][c - 1] > mat[r][c]: 
                #         flag = False 
                # if c + 1 < cols: 
                #     if mat[r][c + 1] > mat[r][c]: 
                #         flag = False 

                # if flag: 
                #     return [r, c]