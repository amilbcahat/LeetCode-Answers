class Solution:
    def doesAliceWin(self, s: str) -> bool:
        preSum = []
        curSum = 0
        for i in range(len(s)): 
            if s[i] in 'aeiou': 
                curSum += 1
            
            preSum.append(curSum)

        return True if preSum and preSum[-1] > 0 else False