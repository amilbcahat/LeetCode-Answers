class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        #Memory Efficient (Greedy) ->
        #Two smallest from each row and then move on to the other until you reach the last row and hence find the answer !
        def get_min_two(row):
            two_smallest = []
            for val , idx in row : 
                if len(two_smallest) < 2 : 
                    two_smallest.append((val , idx))
                elif two_smallest[1][0] > val : 
                    two_smallest.pop()
                    two_smallest.append((val , idx))
                two_smallest.sort()
            return two_smallest 


        N = len(grid)
        first_row = [(val , idx) for idx , val in enumerate(grid[0])]

        dp = get_min_two(first_row)

        for r in range(1 , N):
            next_dp = []
            for curr_c in range(N):
                curr_val = grid[r][curr_c]
                min_val = float("inf")
                for prev_val , prev_c in dp : 
                    if prev_c != curr_c : 
                        min_val = min(min_val , prev_val  + curr_val)

                next_dp.append((min_val , curr_c))
                next_dp = get_min_two(next_dp)

            dp = next_dp

        return min([val for val , idx in dp])



        #Time Efficient -> 
        # N = len(grid)
        # dp = grid[0]

        # for r in range(1 , N):
        #     next_dp =[float("inf")] * N 
        #     for curr_c in range(N):
        #         for prev_c in range(N):
        #             if prev_c != curr_c : 
        #                 next_dp[curr_c] = min(
        #                     next_dp[curr_c] ,
        #                     grid[r][curr_c] + dp[prev_c]  
        #                 )
        #     dp = next_dp

        # return min(dp)
        
        # TLE
        #ROWS , COLS = len(grid) , len(grid[0])

        # cache = {}
        # def dfs(r , c):
        #     if r == ROWS : 
        #         return 0 

        #     if c < 0 or c == COLS : 
        #         return float("inf")

        #     if (r , c) in cache : 
        #         return cache[(r , c)]

           
        #     minTree = float("inf")
        #     #Can choose any element in the column#
        #     for col in range(COLS):
        #         if col != c :
        #             minTree = min(minTree , dfs(r + 1 , col))

        #     pathSum = grid[r][c] + (minTree if minTree != float("inf") else 0)

        #     print(pathSum)

        #     cache[(r , c)] = pathSum 
        #     return cache[(r , c)]

        # res = float("inf")
        
        # for c in range(COLS):
        #     res = min(res , dfs(0 , c))

        # return res 