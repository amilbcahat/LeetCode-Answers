class Solution:
    def beautySum(self, s: str) -> int:
        res = 0 
        visit = set()
        for i in range(len(s)) : 
            count = [0] * 26
            for j in range(i  , len(s)) : 
                # print(s[i:j + 1])
                count[ord(s[j]) - ord("a")] += 1
                maxFreq = float("-inf")
                minFreq = float("inf")

                for c in count : 
                    if c > 0 : 
                        maxFreq = max(maxFreq , c)
                        minFreq = min(minFreq , c)
                
                res += (maxFreq - minFreq)
        
        return res