class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        #Count num of subarrays where curSum <= x 

        def helper(x):
            if x < 0 : 
                return 0 

            res = 0 
            l , cur = 0 , 0 
            for r in range(len(nums)):
                #Pointers to adjust to the goal
                cur += nums[r]
                while cur > x : 
                    cur -= nums[l]
                    l += 1 
                
                #We add sizes , because it tells the number of subarrays ending with that number at that index 
                res += (r - l + 1)
            return res 
        
        #Idea is that if we find number of subarrays with goal <= 2 and goal <= 1 , then if we substract them , then we would find answer for goal == 2
        return helper(goal) - helper(goal - 1)

        #Subarray with K Sum logic !
        # res = 0 
        # curSum = 0 
        # prefixSum = {0 : 1}

        # for n in nums : 
        #     curSum += n 
        #     diff = curSum - goal 
        #     res += prefixSum.get(diff , 0)
        #     prefixSum[curSum] = 1 + prefixSum.get(curSum ,0)

        # return res 