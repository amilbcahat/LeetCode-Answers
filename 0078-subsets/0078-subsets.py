class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        def dfs(i, cur):
            nonlocal res 
            if i >= len(nums):
                res.append(list(cur))
                return 

            #include 
            dfs(i + 1, cur + [nums[i]])
            #skip 
            dfs(i + 1, cur)

        dfs(0, [])
        return res
            
