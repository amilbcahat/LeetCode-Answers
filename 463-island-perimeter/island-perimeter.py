class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS , COLS = len(grid) , len(grid[0])
        visit = set()
        def dfs(r , c):
            if  r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0 :
                print(r , c)
                return 1
            #
            if (r , c) in visit : 
                return 0

            visit.add((r , c))
            count = 0 
            count += dfs(r - 1  , c)
            count += dfs(r + 1  , c)
            count += dfs(r , c - 1)
            count += dfs(r , c + 1)

            return count 

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 : 
                    return dfs(r , c)
        