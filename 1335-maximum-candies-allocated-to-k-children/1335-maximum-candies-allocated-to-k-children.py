class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        l = 1
        r = max(candies) #pile max value 

        def can_distribute_candies(num_of_candies): 
            cnt = 0 #Count of students we can distribute candies to , with this amount of candies in each subpile
            for pile in candies: 
                cnt += pile // num_of_candies
            return cnt >= k 

        res = 0
        while l <= r: 
            mid = (l + r) // 2
            #check validity
            if can_distribute_candies(mid): 
                res = max(res, mid) #If valid , check for next bigger valid option 
                l = mid + 1
            else: 
                r = mid - 1
        return res