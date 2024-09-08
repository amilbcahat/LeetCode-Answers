class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        l = min(bloomDay)
        r = max(bloomDay)

        res = float("inf")

        def possible(day): 
            #Counts the number of possible bouquets 
            cnt = 0 
            bouquets = 0 
            for bloom in bloomDay :
                #Can bloom within the required days limit 
                if bloom <= day : 
                    cnt += 1 
                else : 
                    #grouping the bouquets 
                    bouquets += (cnt // k)
                    cnt = 0 
            bouquets += (cnt // k)
            return bouquets >= m 

        if m * k > len(bloomDay) : 
            #m * k -> No. of flowers 
            #if bouquets cant be built , with the given array of flowers 
            return -1 

        while l <= r  : 
            targetBloomDay = (l + r) // 2 
            # Check for correct bloomDay 
            if possible(targetBloomDay) : 
                res = min(res, targetBloomDay)  
                #If possible result found , then look for minimum result 
                r = targetBloomDay - 1 
            else : 
                #if result not there , then look for it in the right search space 
                l = targetBloomDay + 1 

        return -1 if res == float("inf") else res 