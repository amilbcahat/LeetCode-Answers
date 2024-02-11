class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        #O(n ** 2)
        #Bottom -Up Approach 
        dp= [[0] * (len(s) + 1) for _ in range(len(s) + 1)]
        res = 0 
        #right to left from bottom
        for i in range(len(s)):
            #Traverse till current item
            for j in range(len(s) - 1, i - 1 , -1):
                if s[i] == s[j]:
                    dp[i][j] = 1 if i == j else 2 
                    if i - 1 >= 0 : 
                        dp[i][j] += dp[i - 1][j + 1]
                else:
                    dp[i][j] = dp[i ][j + 1]
                    if i - 1 >= 0 : 
                        dp[i][j] = max(dp[i][j + 1] , dp[i - 1][j])
                res = max(res , dp[i][j])
        return res 

        #Top Down Approach 
        # cache = {}
        # #Much of the logic is borrowed from LCS 
        # def dfs(i , j):
        #     if i < 0 or j == len(s):
        #         return 0 

        #     if (i , j) in cache : 
        #         return cache[(i , j)]

        #     if s[i] == s[j]:
        #         length = 1 if i == j else 2 
        #         #When it is a Pali , keep on search for more length Pali
        #         cache[(i, j)] = length + dfs(i - 1 , j + 1)
        #     else:
        #         #if some s[l] != s[r] , then just skip from left or right , and keep on searching for better alternatives 
        #         #for longest answer 
        #         cache[(i , j)] = max(dfs(i , j + 1) , dfs(i - 1, j))

        #     return cache[(i , j)]
        
        # for i in range(len(s)):
        #     dfs(i , i),  #Odd length Pali  
        #     dfs(i , i + 1) #Even Length Pali

        # return max(cache.values())