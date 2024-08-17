class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        #considering that we got a valid one at last position !
        dp[len(s)] = True 

        #dp[0] tells that if dp[1:] of the array is able to segment or not 
        for i in range(len(s) - 1 , -1 , -1) : 
            for w in wordDict : 
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w : 
                    dp[i] = dp[i + len(w)]
                if dp[i] : 
                    break 

        #If all words are in WordDict then it will reach True first position as well 
        return dp[0]        