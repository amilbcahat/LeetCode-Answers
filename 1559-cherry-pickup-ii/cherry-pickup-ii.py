class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        #Bottom - Up Approach 
        #Since Top down approach , depended on the previous row , we can use optimized memory solution here 
        #We consider each row , to be a sub problem with 3 * 3 grid , so thats why this is 3D approach 
        ROWS , COLS = len(grid) , len(grid[0])

        dp = [[0] * COLS for _ in range(COLS)]

        for r in reversed(range(ROWS)):
            #Reversed range because start from bottom right 
            cur_dp = [[0] * COLS for _ in range(COLS)]
            for c1 in range(COLS - 1):
                #COLS - 1 , to avoid robot1 to get to robot2
                
                for c2 in range(c1 + 1 , COLS):
                    
                    #It must be noted that , we would not want robots to cross paths , as that would not mean any 
                    #difference in the solution , so we take the right part of the grid only (can take left part as well)
                    max_cherries = 0 
                    cherries = grid[r][c1] + grid[r][c2]
                    #Current cherry
                    for c1_d , c2_d in product([-1 , 0 , 1] , [-1 , 0 , 1]):
                        #9 combinations in a row , so these are the subproblems 
                        nc1 , nc2 = c1 + c1_d , c2 + c2_d 
                        if nc1 < 0 or nc2 == COLS : 
                        #We dont take min , max . since we are considering the right part of the grid anyway
                        #We dont consider the Out of boundary conditions
                        #We also dont need to consider c1 == c2 . case .As we had initialized dp matrix with 0's , so it will 
                        #add upto nothing   
                            continue 
                        #Looks over all the subproblems and finds the best sub problem 
                        max_cherries = max(max_cherries , cherries + dp[nc1][nc2])

                    #fill the collected cherries (maximized version) until now 
                    cur_dp[c1][c2] = max_cherries
            #Exchange for memory optimization 
            dp = cur_dp 

        return dp[0][COLS - 1]
    

        #TOP DOWN APPROACH
        # ROWS , COLS = len(grid) , len(grid[0])

        # cache = {}
        # def dfs(r , c1 , c2):
        #     if (r , c1 , c2) in cache :
        #         return cache[(r , c1 , c2)]
        #     #Robots will always have the same row 
        #     #When both Robots are at the same cell , (c1 == c2) its better that they go to diff cell to maximize output and also to 
        #     #to have more ways of maxmizing output , so we dont consider the c1 == c2 case 
        #     if c1 == c2 or min(c1 , c2) < 0 or max(c1 , c2) == COLS :
        #         return 0
            
        #     #When reached base case 
        #     if r == ROWS - 1 : 
        #         return grid[r][c1] + grid[r][c2]
            
        #     res = 0
        #     #d signifies delta 
        #     for c1_d in [-1 , 0 , 1]:
        #         for c2_d in [-1 , 0 , 1]:
        #             #Traversing both Robots 
        #             res = max(res , 
        #             dfs(r + 1, c1 + c1_d , c2 + c2_d)) #We could add it here as well !

        #     #Add current cell value as well 
        #     cache[(r , c1 , c2)] = res + grid[r][c1] + grid[r][c2]

        #     return cache[(r , c1 , c2)]

        # return dfs(0 , 0 , COLS - 1) 
