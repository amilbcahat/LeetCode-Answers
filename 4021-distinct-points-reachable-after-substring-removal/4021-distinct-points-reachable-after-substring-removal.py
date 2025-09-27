class Solution:
    def distinctPoints(self, s: str, k: int) -> int:

        # cache = {}
        got = set()
        
        # def dfs(i, r, c): 
        #     nonlocal newStr
        #     if i == len(newStr): 
        #         got.add((r, c))
        #         return 
                
        #     if newStr[i] == "U": 
        #         dfs(i + 1, r, c + 1)

        #     elif newStr[i] == "D": 
        #         dfs(i + 1, r, c - 1)

        #     elif newStr[i] == "L": 
        #         dfs(i + 1, r - 1, c)

        #     elif newStr[i] == "R": 
        #         dfs(i + 1, r + 1, c)
        
        
        #Generate Strings -> 
        # n = len(s)
        # for i in range(n - k + 1): 
        #     newStr = s[:i] + s[i + k:]
        #     # print(newStr)
        #     # dfs(0, 0, 0)
        #     x = 0
        #     y = 0
        #     for c in newStr: 
        #         if c == "U": 
        #             y += 1
        #         elif c == "D": 
        #             y -= 1
        #         elif c == "L": 
        #             x -= 1
        #         elif c == "R": 
        #              x += 1
            # got.add((x, y))
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
        # k = len(s) - k
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