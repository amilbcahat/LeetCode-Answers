class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        #Bottom up Approach (sort by ages)-> 
        scores = list(zip(ages , scores))
        scores.sort()
        dp = [0] * len(ages)

        for i in range(len(scores)) : 
            #Save this curr score
            curr = scores[i][1]
            dp[i] = curr
            for j in range(i):
                #If previous age scores are less , then only consider them to add 
                if scores[j][1] <= curr:
                    dp[i] = max( dp[i], dp[j] + curr)

        return max(dp)

        # dp = [0] * len(scores)
        # for i in range(len(scores) - 1 , -1 , -1):
        #     for j in range(i + 1 , len(scores)):
        #         if 

        #Top down Approach 
        # scores = list(zip(ages , scores))
        # scores.sort()
        # cache = {}
            
        # def dfs(i , youngAgecurMax ):
        #     if i >= len(scores):
        #         return 0 

        #     if (i , youngAgecurMax ) in cache :
        #         return cache[(i , youngAgecurMax )]

        #     res = float("-inf")
            
        #     include = float("-inf")
        #     if (youngAgecurMax <= scores[i][1])  :
        #         include = scores[i][1] + dfs(i + 1 , max(youngAgecurMax , scores[i][1]))
        #     skip = dfs(i + 1 , youngAgecurMax )

        #     res = max(include , skip)

        #     cache[(i , youngAgecurMax )] = res

        #     return res 

        # return dfs(0 , 0)