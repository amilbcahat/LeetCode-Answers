class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        l = 0 
        res = 0
        letMap = defaultdict(int)
        #Atleast algo with sliding window 
        for r in range(len(s)):
            if s[r] in 'abc': 
                letMap[s[r]] += 1
            
            while l < r and len(letMap) == 3: 
                res += (len(s) - r)
                if s[l] in letMap: 
                    letMap[s[l]] -= 1
                    if letMap[s[l]] == 0:
                        letMap.pop(s[l])
                l += 1

        return res 

