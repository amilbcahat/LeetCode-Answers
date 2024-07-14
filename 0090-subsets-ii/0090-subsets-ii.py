class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, sub) : 
            if i >= len(nums) : 
                res.append(sub.copy())
                return 

            #To include
            sub.append(nums[i])
            dfs(i + 1, sub)
            #To not to include 
            sub.pop()
            #Skip duplicates by not including the Left Subtree in Right subtree 
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1 
            dfs(i + 1, sub)
            
        dfs(0,[] )
        return res 