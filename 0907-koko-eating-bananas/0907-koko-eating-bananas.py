class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)
        #The max value of k will be max pile , since if this pile can be eaten in 1 speed , then others also can be  
        res = r 

        #Then we just do binary search on this range ! 
        while l <= r : 
            k = (l + r ) // 2 

            hours = 0 

            for p in piles : 
                #calculate hours for this k 
                hours += math.ceil(p / k)

            if hours <= h : 
                res = min(res , k)
                #if valid , search for even lesser speed 
                r = k - 1 
            else : 
                #if so less speed , that is not even valid , 
                #Then search for a valid speed
                l = k + 1 

        return res 