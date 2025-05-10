class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        cntZero2 = 0 
        totalNums2 = 0
        for n in nums2: 
            if n == 0: 
                cntZero2 += 1
            totalNums2 += n 


        cntZero1 = 0 
        totalNums1 = 0
        for n in nums1: 
            if n == 0: 
                cntZero1 += 1
            totalNums1 += n 

        
        print(totalNums1, totalNums2, cntZero1, cntZero2)

        ans = -1
        if totalNums1  == totalNums2  : 
            if cntZero1 == 0 and cntZero2 == 0: 
                return totalNums1
            #Tie breaker on zero then 
            moreZero = cntZero1 if cntZero1 > cntZero2 else cntZero2
            if cntZero1 != 0 and cntZero2 != 0: 
                ans = totalNums1 + moreZero
        elif totalNums1 + cntZero1 > totalNums2 + cntZero2: 
            diff = (totalNums1 + cntZero1) - (totalNums2 + cntZero2) 
            if cntZero2 > 0: 
                ans = totalNums1 + cntZero1 
        else: 
            diff = (totalNums2 + cntZero2) - (totalNums1 + cntZero1)
            if cntZero1 > 0: 
                ans = totalNums2 + cntZero2 

        return ans