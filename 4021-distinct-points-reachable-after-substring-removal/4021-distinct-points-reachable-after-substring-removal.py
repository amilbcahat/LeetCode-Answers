class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        #Just use sliding window 
        got = set()
        x = 0
        y = 0 

        for c in s:
            if c == "U": 
                y += 1
            elif c == "D": 
                y -= 1
            elif c == "L": 
                x -= 1
            elif c == "R": 
                x += 1

        totalX = x
        totalY = y
        l = 0

        curX = 0
        curY = 0
        for r in range(len(s)):
            if s[r] == "U": 
                curY += 1
            elif s[r] == "D": 
                curY -= 1
            elif s[r] == "L": 
                curX -= 1
            elif s[r] == "R": 
                curX += 1

            if r - l + 1 > k: 
                if s[l] == "U": 
                    curY -= 1
                elif s[l] == "D": 
                    curY += 1
                elif s[l] == "L": 
                    curX += 1
                elif s[l] == "R": 
                    curX -= 1
                l += 1

            if r - l + 1 == k: 
                got.add((totalX - curX, totalY - curY))


        return len(got)