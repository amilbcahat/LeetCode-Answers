class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def dfs(i, cur): 
            if (i >= len(s) and len(cur) < 4) or len(cur) > 4: 
                return 

            if i >= len(s): 
                final = ".".join(cur)
                if len(final) - 3 == len(s):
                    res.append(".".join(cur))
                return 

            #include in last str 
            cur.append(s[i])
            dfs(i + 1, cur)
            cur.pop()

            cur[-1] = str(int(cur[-1] + s[i]))
            if 0 <= int(cur[-1]) <= 255:
                dfs(i + 1, cur)

            return

        dfs(1, [s[0]])

        return res



