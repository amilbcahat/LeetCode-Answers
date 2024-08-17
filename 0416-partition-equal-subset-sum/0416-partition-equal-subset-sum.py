class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 : 
            return False 

        target = sum(nums) // 2 
        dp = {}
        #Easy way
        def dfs(i , total) : 
            if total == 0 : 
                return True 

            if i >= len(nums) : 
                return False 

            if (i , total) in dp:
                return dp[(i , total)]
            
            #Include 
            res = (dfs(i + 1 , total - nums[i]) or 
            #Pass the subproblem (dont include)
            dfs(i + 1 , total))

            dp[(i , target)] = res

            return res 
        return dfs(0 , target)
        # dp = set()
        # #Base case -> We have a guaranteed 0 , if we dont want to choice any thing 
        # dp.add(0)
        # #Target is half of sum since we are partitioning into two halves ! 
        # target = sum(nums) // 2
        # for i in range(len(nums)-1,-1,-1):
        #     #Making change in cloned dp because we are iterating on it 
        #     nextDP = set(dp)
        #     for t in dp : 
        #         if (t+ nums[i]) == target : 
        #             return True 
        #         nextDP.add(t+nums[i])
        #     dp = nextDP 
        # #If found in dp then we can say that a half equal to target exists ! since half is target and we can reach that it confirms that both will equal to the primary input ! 
        # return True if target in dp else False


        

        