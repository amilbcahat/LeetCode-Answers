class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        #three possibilities 
        prefix = [[0, 0]]
        for i in range(len(s)):
            if s[i] == "0":
                prefix.append([prefix[i][0] + 1, prefix[i][1]])
            else:
                prefix.append([prefix[i][0], prefix[i][1] + 1])

        n = len(s)
        res = float("inf")
        #0 all 

        res = min(res, n - prefix[n][0])

        #1 all 
        res = min(res, prefix[n][0])

        # print(prefix)
        #Some Zeroes then 111... 
        for i in range(1, len(s) + 1): 
            leftCntOne = prefix[i][1]
            rightCntZero = prefix[n][0] - prefix[i][0]

            res = min(res, rightCntZero + leftCntOne)
            # if prefix[i][0] == i: 
            #     res = min(res, prefix[n][0] - prefix[i][0])
            
            # if prefix[n][1] - prefix[i][1] == n - i: 
            #     res = min(res, prefix[i][1])
 
        return res