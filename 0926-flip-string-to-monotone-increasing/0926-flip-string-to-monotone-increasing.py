class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        #three possibilities 
        prefix = [0]
        for i in range(len(s)):
            if s[i] == "0":
                prefix.append(prefix[i] + 1)
            else:
                prefix.append(prefix[i])

        n = len(s)
        res = float("inf")
        #0 all 
        res = min(res, n - prefix[n])

        #1 all 
        res = min(res, prefix[n])

        #Some Zeroes then 111... 
        for i in range(1, len(s) + 1): 
            leftCntOne = i - prefix[i]
            rightCntZero = prefix[n]- prefix[i]

            res = min(res, rightCntZero + leftCntOne)
 
        return res