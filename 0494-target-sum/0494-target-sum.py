class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cache = {}
    
        def dfs(i,total):
            #Out Of Bounds Base Case ! 
            if i == len(nums):
                return 1 if target == total else 0 
            
            #Used Caching !
            if (i,total) in cache : 
                return cache[(i,total)] 

            #Two choices one for positive and one for negative ! 
            cache[(i,total)] = dfs(i+1, total+nums[i]) + dfs(i+1 , total-nums[i]) 

            return cache[(i,total)]

        return dfs(0,0)