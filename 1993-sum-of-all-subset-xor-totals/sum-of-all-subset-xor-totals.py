class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = []
        def dfs(i, path):
            if i == len(nums):
                if path:
                    ans.append(path.copy())
                return  

            # print(path)

            path.append(nums[i])
            dfs(i + 1 ,path )
            path.pop()
            dfs(i + 1, path)

            
            
        dfs(0, [])
        
        res = 0 
        for li in ans : 
            t = 0 
            for n in li : 
                t = t ^ n
            res += t 
        
        return res 
            