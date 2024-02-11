class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        ROWS , COLS = len(grid) , len(grid[0])

        cache = {}
        def dfs(r , c1 , c2):
            if (r , c1 , c2) in cache :
                return cache[(r , c1 , c2)]
            #Robots will always have the same row 
            #When both Robots are at the same cell , (c1 == c2) its better that they go to diff cell to maximize output and also to 
            #to have more ways of maxmizing output , so we dont consider the c1 == c2 case 
            if c1 == c2 or min(c1 , c2) < 0 or max(c1 , c2) == COLS :
                return 0
            
            #When reached base case 
            if r == ROWS - 1 : 
                return grid[r][c1] + grid[r][c2]
            
            res = 0
            #d signifies delta 
            for c1_d in [-1 , 0 , 1]:
                for c2_d in [-1 , 0 , 1]:
                    #Traversing both Robots 
                    res = max(res , 
                    dfs(r + 1, c1 + c1_d , c2 + c2_d)) #We could add it here as well !

            #Add current cell value as well 
            cache[(r , c1 , c2)] = res + grid[r][c1] + grid[r][c2]

            return cache[(r , c1 , c2)]

        return dfs(0 , 0 , COLS - 1) 
