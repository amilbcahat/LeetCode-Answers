class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        ROWS , COLS = len(grid) , len(grid[0])

        def dfs(r , c , visit): 
            if (r < 0 or c < 0 or c == COLS or r == ROWS or grid[r][c] == 0 
            or (r , c) in visit) : 
                return 

            visit.add((r , c))
            dfs(r + 1 , c, visit)
            dfs(r - 1, c, visit)
            dfs(r , c + 1, visit)
            dfs(r , c - 1, visit)



        def count_islands():
            visit = set()
            count = 0 
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 1 and (r , c) not in visit : 
                        dfs(r , c , visit)
                        count += 1

            return count 

        #Remove no land and count , see if result hits
        if count_islands() != 1 : 
            return 0 

        #Remove 1 land and count , see if result hits 

        for r in range(ROWS) : 
            for c in range(COLS) : 
                if grid[r][c] == 0 : 
                    continue 
                grid[r][c] = 0 
                if count_islands() != 1 : 
                    return 1
                grid[r][c] = 1

        #If both remove cases , dont work , then definitely , its 2 removals 

        return 2 
        