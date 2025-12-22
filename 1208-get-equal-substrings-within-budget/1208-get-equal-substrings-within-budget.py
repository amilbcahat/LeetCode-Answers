class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        #Basic Sliding Window , program (substring)
        l = 0 
        maxLen = 0 
        cur = 0 

        for r in range(len(s)):
            cur += abs(ord(s[r]) - ord(t[r]))

            while cur > maxCost :
                cur -= abs(ord(s[l]) - ord(t[l]))
                l += 1 

            
            maxLen = max(maxLen , r - l + 1)

        return maxLen