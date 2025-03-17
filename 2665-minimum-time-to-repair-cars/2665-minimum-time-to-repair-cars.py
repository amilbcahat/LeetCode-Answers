class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        l , r = 1 , ranks[0] * cars * cars 
        res = -1 

        def count_repaired(time): 
            count_cars = 0 
            for r in ranks: 
                count_cars += int(sqrt(time / r))
            return count_cars

        while l <= r : 
            mid = (l + r) // 2
            if count_repaired(mid) >= cars:
                res = mid 
                r = mid - 1
            else: 
                l = mid + 1

        return res 
