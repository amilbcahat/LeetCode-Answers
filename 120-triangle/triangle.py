class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle) + 1)
        #Bottom - up Approach (Simpler , but less memory Effecient !)
        for row in triangle[::-1]:
            for i , n in enumerate(row) : 
                dp[i] = n + min(dp[i] , dp[i + 1])

        return dp[0]

        #Bottom - up Approach !
        #By starting from second last row , hence saving some space !
        # for r  in range(len(triangle) - 2 , -1 , -1):
        #     for j in range(len(triangle[r])) : 
        #         print(triangle[r] , triangle[r + 1])
        #         print(r , j)
        #         triangle[r][j] = triangle[r][j] + min(triangle[r + 1][j] , triangle[r + 1][j + 1])
            
        # return triangle[0][0]

        
        #Top - Down DP Approach !
        # ROWS = len(triangle)
        # dp = {}
        # def dfs(r , i):
        #     if r == ROWS:
        #         return 0 

        #     if (r , i) in dp : 
        #         return dp[(r , i)]

        #     res = 0 
        #     res = min(dfs(r + 1 , i), #Choose left child  
        #     dfs(r + 1 , i + 1)) #Choose right child
        #     res += triangle[r][i]

        #     dp[(r , i)] = res  
        #     return dp[(r , i)]
        
        # return dfs(0 , 0)