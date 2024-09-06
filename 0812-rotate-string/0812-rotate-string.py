class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal) : 
            return False
        
        if s == goal : 
            return True

        last = s[-1]
        first = s[0]

        for i in range(len(s) - 1) : 
            if goal[i] == last and goal[i + 1] == first and (goal[i + 1:] + goal[:i + 1]) == s  : 
                return True 
        return False
