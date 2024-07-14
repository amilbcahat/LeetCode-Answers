class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i ,cur ,total):
            if total == target : 
                res.append(cur.copy())
                return 

            if i >= len(candidates) or total > target : 
                return 

            cur.append(candidates[i])
            dfs(i + 1 , cur , total + candidates[i])

            cur.pop()
            #Skip the duplicate branches , same as Subsets 2
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1 
            dfs(i + 1 , cur , total)
        
        dfs(0 , [] , 0)
        return res 