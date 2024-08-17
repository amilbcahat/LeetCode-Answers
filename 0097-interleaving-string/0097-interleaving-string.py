class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s3) != len(s1) + len(s2) : 
            return False 

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True 

        #We start from len(s1) and len(s2) , it could be we select a char from s1 and not from s2 , similarly , we can consider the vice cersa case
        for i in range(len(s1) , -1 , -1 ):
            for j in range(len(s2), -1 ,-1) : 
                if i < len(s1) and s1[i] == s3[i + j] : 
                    dp[i][j] = dp[i][j] or dp[i + 1][j]
                if j < len(s2) and s2[j] == s3[i + j] : 
                    dp[i][j] = dp[i][j] or dp[i][j + 1]

        return dp[0][0]

        # dp = {}

        # def dfs(i , j): 
        #     if i >= len(s1) and j >= len(s2) : 
        #         return True 

        #     if (i , j) in dp : 
        #         return dp[(i , j)]

        #     ans = False 

        #     if i < len(s1) and s1[i] == s3[i + j] : 
        #         ans = ans or dfs(i + 1 , j)

        #     if j < len(s2) and s2[j] == s3[i + j] : 
        #         ans = ans or dfs(i , j + 1)

        #     dp[(i , j)] = ans 
        #     return ans 

        # return dfs(0 , 0)

            