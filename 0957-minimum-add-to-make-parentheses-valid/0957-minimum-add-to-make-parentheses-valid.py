class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left = right = 0 
        for c in s : 
            if c == "(": 
                right += 1
            elif c == ")": 
                right -= 1 
                if right == -1: 
                    right = 0
                    left += 1

        return left + right 