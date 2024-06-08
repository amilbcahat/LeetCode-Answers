class Solution:
    def romanToInt(self, s: str) -> int:
        numMap = {
            "I" : 1 , 
            "V" : 5 , 
            "X" : 10 , 
            "L" : 50 , 
            "C" : 100 , 
            "D" : 500 , 
            "M" : 1000 
        }

        total = 0 

        for i in range(len(s)):
            if i + 1 < len(s) and numMap[s[i]] < numMap[s[i + 1]]:
                total -= numMap[s[i]]
            else:
                total += numMap[s[i]]

        return total
            