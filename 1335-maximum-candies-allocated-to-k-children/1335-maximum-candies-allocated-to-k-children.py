class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k: 
            return 0

        l = 1
        r = max(candies) #pile max value 

        def valid(amt): 
            cnt = 0
            for pile in candies: 
                savePile = pile
                saveCnt = cnt 
                # print(pile, amt)
                while pile > amt:
                    pileExtracted = (pile // amt)
                    cnt += pileExtracted
                    pile -= (pileExtracted * amt)
                cnt += 1 if pile == amt else 0
                # print(cnt - saveCnt, savePile)
            return cnt >= k

        res = 0
        while l <= r: 
            mid = (l + r) // 2

            #check validity
            if valid(mid): 
                res = max(res, mid)
                l = mid + 1
            else: 
                r = mid - 1

        return res