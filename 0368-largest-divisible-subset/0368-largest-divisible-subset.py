class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        #Solution , done by me , is also there , but tabulation method given by Neetcode is much cleaner
        #
        #Tabulation Medthod 
        nums.sort()
        dp = [[n] for n in nums] #dp[i] = longest starts at i
        res = []
        for i in range(len(nums) -1 , -1 , -1):
            for j in range(i + 1 , len(nums)): 
                if nums[j] % nums[i] == 0 : 
                    tmp = [nums[i]] + dp[j] #dp[j] exchanged with dfs(j)
                    dp[i] = tmp if len(tmp) > len(dp[i]) else dp[i] #dp[i] exchanged with res
            #Get the largest divisible set
            res = dp[i] if len(dp[i]) > len(res) else res 

        return res


        #Single PArameter (Top - Down Approach) O(n) Memory cache
        #Loop and include , the current value
        # nums.sort()
        # cache = {}

        # def dfs(i) : 
        #     if i == len(nums):
        #         return []

        #     if i in cache : 
        #         return cache[i]

        #     res = [nums[i]]
        #     for j in range(i + 1 , len(nums)):
        #         if nums[j] % nums[i] == 0 : 
        #             tmp = [nums[i]] + dfs(j)
        #             if len(tmp) > len(res):
        #                 res = tmp 

        #     cache[i] = res 
        #     return res 

        # res = []
        # #Subsequence starting from every index 
        # for i in range(len(nums)):
        #     tmp = dfs(i)
        #     if len(tmp) > len(res):
        #         res = tmp 

        # return res 
                
        
        #With two parameters(increased memory)

        # nums.sort()
        # cache = {}

        # def dfs( i , prev):
        #     if i == len(nums):
        #         return []

        #     if (i , prev) in cache : 
        #         return cache[(i , prev)]

        #     res = dfs(i + 1 , prev) #skip nums[i]
        #     if nums[i] % prev == 0 :  #O(32 * n ^ 2) , since factors are like 2 , 4 , 6, 8,10 -> until 2 billiom , so max time factors would be 32 (doubling)
        #         tmp = [nums[i]] + dfs(i + 1 , nums[i]) #include 
        #         res = tmp if len(tmp) > len(res) else res 

        #     cache[(i , prev)] = res 
        #     return res 

        # return dfs(0 , 1)