class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        #Solution Description here
        n = len(nums)
        pre = [-1] * n 
        suff = [-1] * n 
        res = [-1] * n 

        pre[0] = nums[0]
        for i in range(1, n): 
            #Here we can see , nums[i] is here, it means 
            #this itself is checking if we can go left or no
            pre[i] = max(nums[i], pre[i - 1])

        suff[n - 1] = nums[n - 1]
        for i in range(n - 2, -1 , -1): 
            suff[i] = min(nums[i], suff[i + 1])

        res[n - 1] = pre[n - 1] # base case, we can reach max from here for sure
        for i in range(n - 2, -1, -1): 
            res[i] = pre[i]
            if pre[i] > suff[i + 1]: 
                #if we can get a higher pre (itself this i is also considered, then we can just get the highest max reachable from the suff side, so we do res[i] = res[i + 1])
                res[i] = res[i + 1]

        return res
    #Confusions - 
    #Why res[i] = res[i + 1] , because it would be always constant or increasing res array?
    #The reason is that since we are traversing from right to left, due to that, we could see bridges build up, then we can look at right and do res[i] = res[i + 1]
    #but once bridge stops, the whatever pre[i... - 1] array is there , we know that bridge wont be created there as well, thats the reason res[i] = res[i + 1], will always be increasing or constant 
