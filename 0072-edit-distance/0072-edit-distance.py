class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(len(word1) + 1) : 
            dp[i][len(word2)] = len(word1) - i 
        for j in range(len(word2) + 1) : 
            dp[len(word1)][j] = len(word2) - j 

        for i in range(len(word1) -1 , -1, -1) : 
            for j in range(len(word2) - 1, -1 ,-1) : 
                if word1[i] == word2[j] : 
                    dp[i][j] = dp[i + 1][j + 1]
                else : 
                    delete = dp[i + 1][j]
                    insert = dp[i][j + 1]
                    replace = dp[i + 1][j + 1]
                    dp[i][j] = 1 + min(delete , insert , replace)

        return dp[0][0]

        # dp = {}
        #Top Down 
        # def dfs(i , j) : 
        #     #Reached and done
        #     if i == len(word1) and j == len(word2): 
        #         return 0 

        #     #Insert WordX(which is not empty) to WordY
        #     if i == len(word1) : 
        #         return len(word2) - j 

        #     if j == len(word2) : 
        #         return len(word1) - i 

        #     if word1[i] == word2[j] : 
        #         #Like LCS
        #         dp[(i , j)] = dfs(i + 1 , j + 1)
        #     else : 
        #         #i moves forward , as it deleted , and j stays 
        #         delete = dfs(i + 1 , j)
        #         #i remains there as intuitvely way say we insert and matched with j , so j moves forward
        #         insert = dfs(i , j + 1)
        #         #matched i and j by replacing so both move forward
        #         replace = dfs(i + 1, j + 1)

        #         dp[(i , j)] = 1 + min(delete , insert , replace)

        #     return dp[(i , j)]

        # return dfs(0 , 0)