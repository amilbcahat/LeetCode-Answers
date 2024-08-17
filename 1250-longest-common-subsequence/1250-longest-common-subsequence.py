class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #Bottom - up Approach 
        #Add one extra row an col for 0 base cases when doing i + 1, j + 1
        # dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        # for i in range(len(text1) - 1, -1 , -1) : 
        #     for j in range(len(text2) - 1, -1 , -1) : 
        #         if text1[i] == text2[j] : 
        #             dp[i][j] = 1 + dp[i + 1][j + 1] 
        #         else : 
        #             dp[i][j] = max(dp[i + 1][j] , dp[i][j + 1])

        # return dp[0][0]

        #Top - Down Approach 
        cache = {}
        def dfs(i , j) : 
            if i >= len(text1) or j >= len(text2) : 
                return 0 

            if (i , j) in cache : 
                return cache[(i , j)]

            if text1[i] == text2[j] : 
                res = 1 + dfs(i + 1 , j + 1)
            else : 
                res = max(dfs(i + 1 , j) , dfs(i, j + 1))

            cache[(i , j)] = res

            return res 

        return dfs(0 , 0)