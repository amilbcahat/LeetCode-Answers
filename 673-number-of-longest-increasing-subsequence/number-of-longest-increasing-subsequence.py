class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {}
        lenLIS , res = 0 , 0 

        for i in range(len(nums) - 1 , -1 , -1):
            maxLen , maxCnt = 1 , 1 
            #For each subproblem 
            for j in range(i + 1 , len(nums)):
                if nums[j] > nums[i]:
                    length , count = dp[j] # subproblem stored 
                    if length + 1 > maxLen : 
                        maxLen , maxCnt = length + 1 , count #update LIS of this subproblem 
                    elif length + 1 == maxLen : 
                        maxCnt += count #Update count (add up similar correct subproblems) , when maxLen is repeated , lead to same length LIS 

            #Globally updated the LIS 
            if maxLen > lenLIS :
                lenLIS , res = maxLen , maxCnt
            elif maxLen == lenLIS : 
                res += maxCnt #counts are also a subproblem , so they get added as well !
            
            dp[i] = [maxLen , maxCnt]

        return res 