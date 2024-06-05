class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS , COLS = len(grid) , len(grid[0])

        ans = [[0] * (ROWS - 2) for _ in range(ROWS - 2)]
        print(ans)

        for r in range(1 , ROWS - 1):
            for c in range(1 , COLS - 1):
                maxVal = 0 

                for i in range(r - 1, r + 2):
                    for j in range(c - 1 , c + 2) : 
                        maxVal = max(maxVal , grid[i][j])
                
                ans[i - 2][j - 2] = maxVal 

        return ans