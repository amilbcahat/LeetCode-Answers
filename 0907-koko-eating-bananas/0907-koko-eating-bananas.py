class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k): 
            hours = 0 
            for p in piles: 
                if k >= p: 
                    hours += 1
                else:
                    hours += math.ceil(p / k)
            return hours <= h

        l = 1
        r = max(piles)
        res = r

        while l <= r: 
            mid = (l + r) // 2
            if check(mid): 
                r = mid - 1
                res = mid 
            else: 
                l = mid + 1

        return res