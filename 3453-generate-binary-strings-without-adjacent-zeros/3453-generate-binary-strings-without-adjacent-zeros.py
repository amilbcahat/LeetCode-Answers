class Solution:
    def validStrings(self, n: int) -> List[str]:

        res = []
        def dfs(st) :
            if len(st) == n :
                res.append("".join(st))
                return 

            if st[-1] == "1":
                dfs(st + ["1"])
                dfs(st + ["0"])
            else :
                #no adjacent zero when last element is zero
                dfs(st + ["1"])

            return 

        
        dfs(["1"])
        dfs(["0"])
        print(res)

        return res
